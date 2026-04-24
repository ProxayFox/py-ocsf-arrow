"""Auto-generated Arrow schema for OCSF object 'function_invocation'.

OCSF version 1.8.0.
"""

import importlib.util
from pathlib import Path

import pyarrow as pa

_OBJECTS_DIR = Path(__file__).parent


def _load_dep(name: str):
    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PARAMETER_SCHEMA = _load_dep("parameter").PARAMETER_SCHEMA


def get_function_invocation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'function_invocation'."""
    return pa.schema(
        [
            pa.field("error", pa.string(), nullable=True),
            pa.field(
                "parameters",
                pa.list_(pa.struct(list(PARAMETER_SCHEMA))),
                nullable=True,
            ),
            pa.field("return_value", pa.string(), nullable=True),
        ]
    )


FUNCTION_INVOCATION_SCHEMA = get_function_invocation_schema()
