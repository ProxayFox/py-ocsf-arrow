"""Auto-generated OCSF category schema exports.

Class files have numeric-prefixed names which Python cannot import with
a normal ``import`` statement.  They are loaded via ``importlib`` and
exposed as a stable API from this package.
"""

from __future__ import annotations

from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType


@lru_cache(maxsize=1)
def _load_inventory_info_module() -> ModuleType:
    module_path = Path(__file__).with_name("5001_inventory_info.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.5_discovery._5001_inventory_info",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_inventory_info_schema():
    """Return the generated Arrow schema for OCSF class 5001."""
    return _load_inventory_info_module().get_inventory_info_schema()


INVENTORY_INFO_SCHEMA = get_inventory_info_schema()


@lru_cache(maxsize=1)
def _load_config_state_module() -> ModuleType:
    module_path = Path(__file__).with_name("5002_config_state.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.5_discovery._5002_config_state",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_config_state_schema():
    """Return the generated Arrow schema for OCSF class 5002."""
    return _load_config_state_module().get_config_state_schema()


CONFIG_STATE_SCHEMA = get_config_state_schema()


__all__ = [
    "get_inventory_info_schema",
    "INVENTORY_INFO_SCHEMA",
    "get_config_state_schema",
    "CONFIG_STATE_SCHEMA",
]
