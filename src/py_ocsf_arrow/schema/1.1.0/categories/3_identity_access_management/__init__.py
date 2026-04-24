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
def _load_account_change_module() -> ModuleType:
    module_path = Path(__file__).with_name("3001_account_change.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3001_account_change",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_account_change_schema():
    """Return the generated Arrow schema for OCSF class 3001."""
    return _load_account_change_module().get_account_change_schema()


ACCOUNT_CHANGE_SCHEMA = get_account_change_schema()


@lru_cache(maxsize=1)
def _load_authentication_module() -> ModuleType:
    module_path = Path(__file__).with_name("3002_authentication.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3002_authentication",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_authentication_schema():
    """Return the generated Arrow schema for OCSF class 3002."""
    return _load_authentication_module().get_authentication_schema()


AUTHENTICATION_SCHEMA = get_authentication_schema()


@lru_cache(maxsize=1)
def _load_authorize_session_module() -> ModuleType:
    module_path = Path(__file__).with_name("3003_authorize_session.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3003_authorize_session",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_authorize_session_schema():
    """Return the generated Arrow schema for OCSF class 3003."""
    return _load_authorize_session_module().get_authorize_session_schema()


AUTHORIZE_SESSION_SCHEMA = get_authorize_session_schema()


@lru_cache(maxsize=1)
def _load_entity_management_module() -> ModuleType:
    module_path = Path(__file__).with_name("3004_entity_management.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3004_entity_management",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_entity_management_schema():
    """Return the generated Arrow schema for OCSF class 3004."""
    return _load_entity_management_module().get_entity_management_schema()


ENTITY_MANAGEMENT_SCHEMA = get_entity_management_schema()


@lru_cache(maxsize=1)
def _load_user_access_module() -> ModuleType:
    module_path = Path(__file__).with_name("3005_user_access.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3005_user_access",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_user_access_schema():
    """Return the generated Arrow schema for OCSF class 3005."""
    return _load_user_access_module().get_user_access_schema()


USER_ACCESS_SCHEMA = get_user_access_schema()


@lru_cache(maxsize=1)
def _load_group_management_module() -> ModuleType:
    module_path = Path(__file__).with_name("3006_group_management.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management._3006_group_management",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = (
        "py_ocsf_arrow.schema.1.1.0.categories.3_identity_access_management"
    )
    spec.loader.exec_module(module)
    return module


def get_group_management_schema():
    """Return the generated Arrow schema for OCSF class 3006."""
    return _load_group_management_module().get_group_management_schema()


GROUP_MANAGEMENT_SCHEMA = get_group_management_schema()


__all__ = [
    "get_account_change_schema",
    "ACCOUNT_CHANGE_SCHEMA",
    "get_authentication_schema",
    "AUTHENTICATION_SCHEMA",
    "get_authorize_session_schema",
    "AUTHORIZE_SESSION_SCHEMA",
    "get_entity_management_schema",
    "ENTITY_MANAGEMENT_SCHEMA",
    "get_user_access_schema",
    "USER_ACCESS_SCHEMA",
    "get_group_management_schema",
    "GROUP_MANAGEMENT_SCHEMA",
]
