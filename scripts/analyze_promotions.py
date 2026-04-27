from __future__ import annotations

import json
import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Iterable
from pathlib import Path
from typing import TextIO

import pyarrow as pa

from ocsf.api.client import OcsfApiClient

from py_ocsf_arrow import SchemaGenerator
from py_ocsf_arrow.base import CACHE_DIR
from py_ocsf_arrow.promotion import ScoringConfig, Verdict, run_promotion_analysis
from py_ocsf_arrow.promotion_report import format_summary, to_csv, to_json
from py_ocsf_arrow.schema_transform import (
    TransformConfig,
    TransformResult,
    apply_promotions,
)


def parse_override(value: str) -> tuple[str, Verdict]:
    """Parse one ``NAME=VERDICT`` override pair."""

    if "=" not in value:
        raise ValueError(
            f"Invalid override format. Expected NAME=VERDICT, got {value!r}."
        )

    name, verdict_text = value.split("=", 1)
    name = name.strip()
    verdict_key = verdict_text.strip().upper()
    if not name or not verdict_key:
        raise ValueError(
            f"Invalid override format. Expected NAME=VERDICT, got {value!r}."
        )

    try:
        verdict = Verdict[verdict_key]
    except KeyError as exc:
        allowed = ", ".join(verdict.value for verdict in Verdict)
        raise ValueError(
            f"Invalid override verdict {verdict_text!r}. Expected one of: {allowed}."
        ) from exc

    return name, verdict


def parse_overrides(values: Iterable[str]) -> dict[str, Verdict]:
    """Parse repeated ``--override`` values into a verdict map."""

    return dict(parse_override(value) for value in values)


def build_scoring_config(args: Namespace) -> ScoringConfig:
    """Build a scoring config from parsed CLI arguments."""

    config = ScoringConfig()
    if args.promote_threshold is not None:
        config.promote_threshold = args.promote_threshold
    if args.review_threshold is not None:
        config.review_threshold = args.review_threshold
    config.__post_init__()
    return config


def resolve_version(client: OcsfApiClient, version: str) -> str:
    """Resolve ``default`` and validate explicit versions."""

    if version == "default":
        return client.get_default_version()

    versions = client.get_versions()
    if version not in versions:
        raise ValueError(f"Unknown OCSF version: {version}")
    return version


def load_schema(client: OcsfApiClient, version: str):
    """Load the requested OCSF schema using the repo's normal client flow."""

    resolved_version = resolve_version(client, version)
    return resolved_version, client.get_schema(version=resolved_version)


def format_summary_with_scores(results) -> str:
    """Return summary output with an additional per-object score breakdown."""

    lines = [format_summary(results), "", "Per-object score breakdown:"]
    for result in results:
        lines.append(
            "  "
            f"{result.name}: verdict={result.verdict.value} "
            f"composite={result.composite_score:.6f} "
            f"complexity={result.complexity_score:.6f} "
            f"connectivity={result.connectivity_score:.6f} "
            f"entity={result.entity_score:.6f} "
            f"storage={result.storage_amplification_score:.6f} "
            f"queryability={result.queryability_score:.6f}"
        )
    return "\n".join(lines)


def render_report(results, output_format: str, include_scores: bool) -> str:
    """Render the requested report format."""

    if output_format == "json":
        return to_json(results)
    if output_format == "csv":
        return to_csv(results)
    if include_scores:
        return format_summary_with_scores(results)
    return format_summary(results)


def write_output(content: str, output_path: str | None, stdout: TextIO) -> None:
    """Write report content either to stdout or a target file."""

    if output_path is None:
        stdout.write(content)
        if not content.endswith("\n"):
            stdout.write("\n")
        return

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        content if content.endswith("\n") else f"{content}\n", encoding="utf-8"
    )


def build_class_schemas(
    version: str, client: OcsfApiClient
) -> tuple[str, dict[str, pa.Schema], object]:
    """Build base-only class schemas for the requested version."""

    generator = SchemaGenerator.init(version=version, client=client)
    class_schemas = {
        class_name: generator.build_class_schema(class_name)
        for class_name in sorted(generator.schema.classes)
    }
    return generator.version, class_schemas, generator.schema


def _count_fk_fields(schemas: Iterable[pa.Schema]) -> int:
    """Count fields carrying FK metadata across the provided schemas."""

    return sum(
        1
        for schema in schemas
        for field in schema
        if (field.metadata or {}).get(b"ocsf.ref_table")
    )


def _safe_schema_file_stem(schema_name: str) -> str:
    """Return a filesystem-safe filename stem for a schema name."""

    return schema_name.replace("/", "__")


def write_transform_output(directory: str, result: TransformResult) -> Path:
    """Write transformed schemas as Arrow-serialized schema files."""

    root = Path(directory)
    classes_dir = root / "classes"
    promoted_dir = root / "promoted"
    classes_dir.mkdir(parents=True, exist_ok=True)
    promoted_dir.mkdir(parents=True, exist_ok=True)

    for schema_name, schema in result.class_schemas.items():
        safe_name = _safe_schema_file_stem(schema_name)
        (classes_dir / f"{safe_name}.arrow").write_bytes(
            schema.serialize().to_pybytes()
        )

    for schema_name, schema in result.promoted_schemas.items():
        safe_name = _safe_schema_file_stem(schema_name)
        (promoted_dir / f"{safe_name}.arrow").write_bytes(
            schema.serialize().to_pybytes()
        )

    manifest = {
        "class_schema_count": len(result.class_schemas),
        "promoted_schema_count": len(result.promoted_schemas),
        "warning_count": len(result.warnings),
        "warnings": result.warnings,
    }
    (root / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return root


def write_transform_summary(result: TransformResult, stderr: TextIO) -> None:
    """Write operator-facing transform summary information to stderr."""

    fk_fields = _count_fk_fields(result.class_schemas.values()) + _count_fk_fields(
        result.promoted_schemas.values()
    )
    stderr.write("Transform summary\n")
    stderr.write(f"Class schemas transformed: {len(result.class_schemas)}\n")
    stderr.write(f"Promoted object schemas generated: {len(result.promoted_schemas)}\n")
    stderr.write(f"FK fields created: {fk_fields}\n")
    stderr.write(f"Warnings: {len(result.warnings)}\n")


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description=(
            "Run OCSF object-promotion analysis and optionally transform class "
            "schemas using the promotion verdicts."
        )
    )
    parser.add_argument(
        "--version",
        required=True,
        help='OCSF schema version to analyze (for example "1.8.0" or "default")',
    )
    parser.add_argument(
        "--override",
        action="append",
        default=[],
        help=(
            "Force a verdict for a specific object. Repeat as needed, for "
            "example --override metadata=EMBED --override endpoint=EMBED"
        ),
    )
    parser.add_argument(
        "--promote-threshold",
        type=float,
        default=None,
        help="Composite score threshold for PROMOTE (default: ScoringConfig default)",
    )
    parser.add_argument(
        "--review-threshold",
        type=float,
        default=None,
        help="Composite score threshold for REVIEW (default: ScoringConfig default)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "json", "csv"),
        default="summary",
        help='Analysis output format (default: "summary")',
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Write analysis output to a file instead of stdout",
    )
    parser.add_argument(
        "--include-scores",
        action="store_true",
        help="In summary mode, include per-axis scores for every object",
    )
    parser.add_argument(
        "--transform",
        action="store_true",
        help="Enable the full promotion + schema transformation pipeline",
    )
    parser.add_argument(
        "--strict-review",
        action="store_true",
        help="Fail in transform mode when any object remains REVIEW",
    )
    parser.add_argument(
        "--transform-output",
        default=None,
        help="Directory for writing transformed schemas (.arrow files)",
    )
    return parser


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    args = build_parser().parse_args(argv)
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr

    try:
        overrides = parse_overrides(args.override)
        scoring_config = build_scoring_config(args)
        client = OcsfApiClient(cache_dir=CACHE_DIR)
        resolved_version, schema = load_schema(client, args.version)
        analyses = run_promotion_analysis(
            schema,
            config=scoring_config,
            overrides=overrides,
        )
        report = render_report(analyses, args.format, args.include_scores)
        write_output(report, args.output, stdout)

        if not args.transform:
            return 0

        _, class_schemas, transform_schema = build_class_schemas(
            resolved_version, client
        )
        transform_result = apply_promotions(
            class_schemas,
            transform_schema,
            analyses,
            TransformConfig(strict_review=args.strict_review),
            overrides=overrides,
        )
        if args.transform_output is not None:
            write_transform_output(args.transform_output, transform_result)
        write_transform_summary(transform_result, stderr)
        return 0
    except ValueError as exc:
        stderr.write(f"Error: {exc}\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
