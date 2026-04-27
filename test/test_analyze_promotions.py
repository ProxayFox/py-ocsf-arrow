from __future__ import annotations

import csv
import io
import json
from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

import pytest

from py_ocsf_arrow.promotion import ScoringConfig, Verdict

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "analyze_promotions.py"


@pytest.fixture(scope="module")
def analyze_module() -> ModuleType:
    spec = spec_from_file_location("_analyze_promotions", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_help_text_lists_key_arguments(analyze_module: ModuleType):
    stdout = io.StringIO()

    with pytest.raises(SystemExit) as exc, redirect_stdout(stdout):
        analyze_module.build_parser().parse_args(["--help"])

    output = stdout.getvalue()
    assert exc.value.code == 0
    assert "--version" in output
    assert "--override" in output
    assert "--transform" in output
    assert "--strict-review" in output
    assert "--transform-output" in output


def test_override_parsing_valid_and_multiple(analyze_module: ModuleType):
    assert analyze_module.parse_override("metadata=EMBED") == (
        "metadata",
        Verdict.EMBED,
    )
    assert analyze_module.parse_overrides(["metadata=EMBED", "endpoint=EMBED"]) == {
        "metadata": Verdict.EMBED,
        "endpoint": Verdict.EMBED,
    }


def test_override_parsing_invalid_format(analyze_module: ModuleType):
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = analyze_module.main(
        ["--version", "1.8.0", "--override", "metadata"],
        stdout=stdout,
        stderr=stderr,
    )

    assert exit_code == 1
    assert "Invalid override format" in stderr.getvalue()


def test_threshold_parsing_updates_scoring_config(analyze_module: ModuleType):
    args = analyze_module.build_parser().parse_args(
        ["--version", "1.8.0", "--promote-threshold", "0.7"]
    )

    config = analyze_module.build_scoring_config(args)

    assert isinstance(config, ScoringConfig)
    assert config.promote_threshold == pytest.approx(0.7)
    assert config.review_threshold == pytest.approx(ScoringConfig().review_threshold)


def test_format_json_output_is_valid(analyze_module: ModuleType):
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--format",
            "json",
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    payload = json.loads(stdout.getvalue())
    assert exit_code == 0
    assert isinstance(payload, list)
    assert any(item["name"] == "device" for item in payload)
    assert stderr.getvalue() == ""


def test_format_csv_output_is_valid(analyze_module: ModuleType):
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--format",
            "csv",
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    rows = list(csv.DictReader(io.StringIO(stdout.getvalue())))
    assert exit_code == 0
    assert rows
    assert any(row["name"] == "device" for row in rows)
    assert stderr.getvalue() == ""


def test_default_format_is_summary(analyze_module: ModuleType):
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    output = stdout.getvalue()
    assert exit_code == 0
    assert "Promotion analysis summary" in output
    assert "PROMOTE objects:" in output
    assert "device" in output
    assert stderr.getvalue() == ""


def test_output_to_file(analyze_module: ModuleType, tmp_path: Path):
    stdout = io.StringIO()
    stderr = io.StringIO()
    output_path = tmp_path / "analysis.txt"

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--output",
            str(output_path),
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    assert exit_code == 0
    assert stdout.getvalue() == ""
    assert output_path.exists()
    assert "Promotion analysis summary" in output_path.read_text(encoding="utf-8")
    assert stderr.getvalue() == ""


def test_analysis_only_mode_live_schema(analyze_module: ModuleType):
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    output = stdout.getvalue()
    assert exit_code == 0
    assert "metadata" in output
    assert "osint" in output
    assert "device" in output
    assert stderr.getvalue() == ""


def test_transform_mode_writes_summary_and_files(
    analyze_module: ModuleType, tmp_path: Path
):
    stdout = io.StringIO()
    stderr = io.StringIO()
    output_dir = tmp_path / "transform-output"

    exit_code = analyze_module.main(
        [
            "--version",
            "1.8.0",
            "--transform",
            "--transform-output",
            str(output_dir),
            "--override",
            "metadata=EMBED",
            "--override",
            "endpoint=EMBED",
        ],
        stdout=stdout,
        stderr=stderr,
    )

    stderr_output = stderr.getvalue()
    assert exit_code == 0
    assert "Promotion analysis summary" in stdout.getvalue()
    assert "Transform summary" in stderr_output
    assert "Class schemas transformed:" in stderr_output
    assert "Promoted object schemas generated:" in stderr_output
    assert (output_dir / "classes").exists()
    assert (output_dir / "promoted").exists()
    assert list((output_dir / "classes").glob("*.arrow"))
    assert (output_dir / "manifest.json").exists()
