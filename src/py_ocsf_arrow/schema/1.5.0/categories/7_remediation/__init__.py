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
def _load_remediation_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("7001_remediation_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.5.0.categories.7_remediation._7001_remediation_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.5.0.categories.7_remediation"
    spec.loader.exec_module(module)
    return module


def get_remediation_activity_schema():
    """Return the generated Arrow schema for OCSF class 7001."""
    return _load_remediation_activity_module().get_remediation_activity_schema()


REMEDIATION_ACTIVITY_SCHEMA = get_remediation_activity_schema()


@lru_cache(maxsize=1)
def _load_file_remediation_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("7002_file_remediation_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.5.0.categories.7_remediation._7002_file_remediation_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.5.0.categories.7_remediation"
    spec.loader.exec_module(module)
    return module


def get_file_remediation_activity_schema():
    """Return the generated Arrow schema for OCSF class 7002."""
    return (
        _load_file_remediation_activity_module().get_file_remediation_activity_schema()
    )


FILE_REMEDIATION_ACTIVITY_SCHEMA = get_file_remediation_activity_schema()


@lru_cache(maxsize=1)
def _load_process_remediation_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("7003_process_remediation_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.5.0.categories.7_remediation._7003_process_remediation_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.5.0.categories.7_remediation"
    spec.loader.exec_module(module)
    return module


def get_process_remediation_activity_schema():
    """Return the generated Arrow schema for OCSF class 7003."""
    return _load_process_remediation_activity_module().get_process_remediation_activity_schema()


PROCESS_REMEDIATION_ACTIVITY_SCHEMA = get_process_remediation_activity_schema()


@lru_cache(maxsize=1)
def _load_network_remediation_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("7004_network_remediation_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.5.0.categories.7_remediation._7004_network_remediation_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.5.0.categories.7_remediation"
    spec.loader.exec_module(module)
    return module


def get_network_remediation_activity_schema():
    """Return the generated Arrow schema for OCSF class 7004."""
    return _load_network_remediation_activity_module().get_network_remediation_activity_schema()


NETWORK_REMEDIATION_ACTIVITY_SCHEMA = get_network_remediation_activity_schema()


__all__ = [
    "get_remediation_activity_schema",
    "REMEDIATION_ACTIVITY_SCHEMA",
    "get_file_remediation_activity_schema",
    "FILE_REMEDIATION_ACTIVITY_SCHEMA",
    "get_process_remediation_activity_schema",
    "PROCESS_REMEDIATION_ACTIVITY_SCHEMA",
    "get_network_remediation_activity_schema",
    "NETWORK_REMEDIATION_ACTIVITY_SCHEMA",
]
