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
def _load_web_resources_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("6001_web_resources_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity._6001_web_resources_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity"
    spec.loader.exec_module(module)
    return module


def get_web_resources_activity_schema():
    """Return the generated Arrow schema for OCSF class 6001."""
    return _load_web_resources_activity_module().get_web_resources_activity_schema()


WEB_RESOURCES_ACTIVITY_SCHEMA = get_web_resources_activity_schema()


@lru_cache(maxsize=1)
def _load_application_lifecycle_module() -> ModuleType:
    module_path = Path(__file__).with_name("6002_application_lifecycle.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity._6002_application_lifecycle",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity"
    spec.loader.exec_module(module)
    return module


def get_application_lifecycle_schema():
    """Return the generated Arrow schema for OCSF class 6002."""
    return _load_application_lifecycle_module().get_application_lifecycle_schema()


APPLICATION_LIFECYCLE_SCHEMA = get_application_lifecycle_schema()


@lru_cache(maxsize=1)
def _load_api_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("6003_api_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity._6003_api_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity"
    spec.loader.exec_module(module)
    return module


def get_api_activity_schema():
    """Return the generated Arrow schema for OCSF class 6003."""
    return _load_api_activity_module().get_api_activity_schema()


API_ACTIVITY_SCHEMA = get_api_activity_schema()


@lru_cache(maxsize=1)
def _load_web_resource_access_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("6004_web_resource_access_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity._6004_web_resource_access_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.0.0.categories.6_application_activity"
    spec.loader.exec_module(module)
    return module


def get_web_resource_access_activity_schema():
    """Return the generated Arrow schema for OCSF class 6004."""
    return _load_web_resource_access_activity_module().get_web_resource_access_activity_schema()


WEB_RESOURCE_ACCESS_ACTIVITY_SCHEMA = get_web_resource_access_activity_schema()


__all__ = [
    "get_web_resources_activity_schema",
    "WEB_RESOURCES_ACTIVITY_SCHEMA",
    "get_application_lifecycle_schema",
    "APPLICATION_LIFECYCLE_SCHEMA",
    "get_api_activity_schema",
    "API_ACTIVITY_SCHEMA",
    "get_web_resource_access_activity_schema",
    "WEB_RESOURCE_ACCESS_ACTIVITY_SCHEMA",
]
