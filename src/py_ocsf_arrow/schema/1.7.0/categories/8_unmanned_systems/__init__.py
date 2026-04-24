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
def _load_drone_flights_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("8001_drone_flights_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.7.0.categories.8_unmanned_systems._8001_drone_flights_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.7.0.categories.8_unmanned_systems"
    spec.loader.exec_module(module)
    return module


def get_drone_flights_activity_schema():
    """Return the generated Arrow schema for OCSF class 8001."""
    return _load_drone_flights_activity_module().get_drone_flights_activity_schema()


DRONE_FLIGHTS_ACTIVITY_SCHEMA = get_drone_flights_activity_schema()


@lru_cache(maxsize=1)
def _load_airborne_broadcast_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("8002_airborne_broadcast_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.7.0.categories.8_unmanned_systems._8002_airborne_broadcast_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.7.0.categories.8_unmanned_systems"
    spec.loader.exec_module(module)
    return module


def get_airborne_broadcast_activity_schema():
    """Return the generated Arrow schema for OCSF class 8002."""
    return _load_airborne_broadcast_activity_module().get_airborne_broadcast_activity_schema()


AIRBORNE_BROADCAST_ACTIVITY_SCHEMA = get_airborne_broadcast_activity_schema()


__all__ = [
    "get_drone_flights_activity_schema",
    "DRONE_FLIGHTS_ACTIVITY_SCHEMA",
    "get_airborne_broadcast_activity_schema",
    "AIRBORNE_BROADCAST_ACTIVITY_SCHEMA",
]
