from __future__ import annotations

from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path
import json
from typing import cast

import pyarrow as pa

from py_ocsf_arrow import SchemaGenerator


def _render_type(data_type: pa.DataType) -> str:
    """Render a PyArrow DataType as a Python expression."""
    if data_type == pa.bool8():
        return "pa.bool8()"
    if pa.types.is_boolean(data_type):
        return "pa.bool_()"
    if pa.types.is_int8(data_type):
        return "pa.int8()"
    if pa.types.is_int16(data_type):
        return "pa.int16()"
    if pa.types.is_int32(data_type):
        return "pa.int32()"
    if pa.types.is_int64(data_type):
        return "pa.int64()"
    if pa.types.is_uint8(data_type):
        return "pa.uint8()"
    if pa.types.is_uint16(data_type):
        return "pa.uint16()"
    if pa.types.is_uint32(data_type):
        return "pa.uint32()"
    if pa.types.is_uint64(data_type):
        return "pa.uint64()"
    if pa.types.is_float16(data_type):
        return "pa.float16()"
    if pa.types.is_float32(data_type):
        return "pa.float32()"
    if pa.types.is_float64(data_type):
        return "pa.float64()"
    if pa.types.is_string(data_type):
        return "pa.string()"
    if pa.types.is_large_string(data_type):
        return "pa.large_string()"
    if pa.types.is_binary(data_type):
        return "pa.binary()"
    if pa.types.is_large_binary(data_type):
        return "pa.large_binary()"
    if pa.types.is_list(data_type):
        list_type = cast(pa.ListType, data_type)
        return f"pa.list_({_render_type(list_type.value_type)})"
    if pa.types.is_large_list(data_type):
        large_list_type = cast(pa.LargeListType, data_type)
        return f"pa.large_list({_render_type(large_list_type.value_type)})"
    if pa.types.is_struct(data_type):
        struct_type = cast(pa.StructType, data_type)
        parts = [
            f"pa.field({json.dumps(field.name)}, {_render_type(field.type)}, nullable={field.nullable})"
            for field in struct_type
        ]
        return "pa.struct([" + ", ".join(parts) + "])"
    raise ValueError(f"Unsupported PyArrow data type for rendering: {data_type}")


def _render_schema_module(schema: pa.Schema, class_name: str, version: str) -> str:
    fn_name = f"get_{class_name}_schema"
    const_name = f"{class_name.upper()}_SCHEMA"
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    rendered_fields = "\n".join(
        f"        pa.field({json.dumps(field.name)}, {_render_type(field.type)}, nullable={field.nullable}),"
        for field in schema
    )

    return (
        '"""Auto-generated Arrow schema module.\n\n'
        f"Generated from OCSF class '{class_name}' (version={version}) at {timestamp}.\n"
        '"""\n\n'
        "import pyarrow as pa\n\n\n"
        f"def {fn_name}() -> pa.Schema:\n"
        '    """Return the Arrow schema for this OCSF class."""\n'
        "    return pa.schema(\n"
        "        [\n"
        f"{rendered_fields}\n"
        "        ]\n"
        "    )\n\n\n"
        f"{const_name} = {fn_name}()\n"
    )


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Generate a Python schema module from an OCSF class schema."
    )
    parser.add_argument(
        "--class-name",
        default="vulnerability_finding",
        help="OCSF class name to render (default: vulnerability_finding)",
    )
    parser.add_argument(
        "--version",
        default="default",
        help="OCSF schema version (default: default)",
    )
    parser.add_argument(
        "--output",
        default="src/py_ocsf_arrow/schema/findings/2002_vulnerability_finding.py",
        help="Output Python file path",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    generator = SchemaGenerator.init(version=args.version)
    schema = generator.build_class_schema(args.class_name)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    module_content = _render_schema_module(
        schema=schema,
        class_name=args.class_name,
        version=generator.version,
    )
    output_path.write_text(module_content, encoding="utf-8")

    print(f"Wrote schema module: {output_path}")


if __name__ == "__main__":
    main()
