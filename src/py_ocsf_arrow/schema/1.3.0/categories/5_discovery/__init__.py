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
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5001_inventory_info",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
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
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5002_config_state",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_config_state_schema():
    """Return the generated Arrow schema for OCSF class 5002."""
    return _load_config_state_module().get_config_state_schema()


CONFIG_STATE_SCHEMA = get_config_state_schema()


@lru_cache(maxsize=1)
def _load_user_inventory_module() -> ModuleType:
    module_path = Path(__file__).with_name("5003_user_inventory.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5003_user_inventory",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_user_inventory_schema():
    """Return the generated Arrow schema for OCSF class 5003."""
    return _load_user_inventory_module().get_user_inventory_schema()


USER_INVENTORY_SCHEMA = get_user_inventory_schema()


@lru_cache(maxsize=1)
def _load_patch_state_module() -> ModuleType:
    module_path = Path(__file__).with_name("5004_patch_state.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5004_patch_state",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_patch_state_schema():
    """Return the generated Arrow schema for OCSF class 5004."""
    return _load_patch_state_module().get_patch_state_schema()


PATCH_STATE_SCHEMA = get_patch_state_schema()


@lru_cache(maxsize=1)
def _load_kernel_object_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5006_kernel_object_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5006_kernel_object_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_kernel_object_query_schema():
    """Return the generated Arrow schema for OCSF class 5006."""
    return _load_kernel_object_query_module().get_kernel_object_query_schema()


KERNEL_OBJECT_QUERY_SCHEMA = get_kernel_object_query_schema()


@lru_cache(maxsize=1)
def _load_file_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5007_file_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5007_file_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_file_query_schema():
    """Return the generated Arrow schema for OCSF class 5007."""
    return _load_file_query_module().get_file_query_schema()


FILE_QUERY_SCHEMA = get_file_query_schema()


@lru_cache(maxsize=1)
def _load_folder_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5008_folder_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5008_folder_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_folder_query_schema():
    """Return the generated Arrow schema for OCSF class 5008."""
    return _load_folder_query_module().get_folder_query_schema()


FOLDER_QUERY_SCHEMA = get_folder_query_schema()


@lru_cache(maxsize=1)
def _load_admin_group_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5009_admin_group_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5009_admin_group_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_admin_group_query_schema():
    """Return the generated Arrow schema for OCSF class 5009."""
    return _load_admin_group_query_module().get_admin_group_query_schema()


ADMIN_GROUP_QUERY_SCHEMA = get_admin_group_query_schema()


@lru_cache(maxsize=1)
def _load_job_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5010_job_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5010_job_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_job_query_schema():
    """Return the generated Arrow schema for OCSF class 5010."""
    return _load_job_query_module().get_job_query_schema()


JOB_QUERY_SCHEMA = get_job_query_schema()


@lru_cache(maxsize=1)
def _load_module_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5011_module_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5011_module_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_module_query_schema():
    """Return the generated Arrow schema for OCSF class 5011."""
    return _load_module_query_module().get_module_query_schema()


MODULE_QUERY_SCHEMA = get_module_query_schema()


@lru_cache(maxsize=1)
def _load_network_connection_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5012_network_connection_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5012_network_connection_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_network_connection_query_schema():
    """Return the generated Arrow schema for OCSF class 5012."""
    return _load_network_connection_query_module().get_network_connection_query_schema()


NETWORK_CONNECTION_QUERY_SCHEMA = get_network_connection_query_schema()


@lru_cache(maxsize=1)
def _load_networks_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5013_networks_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5013_networks_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_networks_query_schema():
    """Return the generated Arrow schema for OCSF class 5013."""
    return _load_networks_query_module().get_networks_query_schema()


NETWORKS_QUERY_SCHEMA = get_networks_query_schema()


@lru_cache(maxsize=1)
def _load_peripheral_device_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5014_peripheral_device_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5014_peripheral_device_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_peripheral_device_query_schema():
    """Return the generated Arrow schema for OCSF class 5014."""
    return _load_peripheral_device_query_module().get_peripheral_device_query_schema()


PERIPHERAL_DEVICE_QUERY_SCHEMA = get_peripheral_device_query_schema()


@lru_cache(maxsize=1)
def _load_process_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5015_process_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5015_process_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_process_query_schema():
    """Return the generated Arrow schema for OCSF class 5015."""
    return _load_process_query_module().get_process_query_schema()


PROCESS_QUERY_SCHEMA = get_process_query_schema()


@lru_cache(maxsize=1)
def _load_service_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5016_service_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5016_service_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_service_query_schema():
    """Return the generated Arrow schema for OCSF class 5016."""
    return _load_service_query_module().get_service_query_schema()


SERVICE_QUERY_SCHEMA = get_service_query_schema()


@lru_cache(maxsize=1)
def _load_session_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5017_session_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5017_session_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_session_query_schema():
    """Return the generated Arrow schema for OCSF class 5017."""
    return _load_session_query_module().get_session_query_schema()


SESSION_QUERY_SCHEMA = get_session_query_schema()


@lru_cache(maxsize=1)
def _load_user_query_module() -> ModuleType:
    module_path = Path(__file__).with_name("5018_user_query.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5018_user_query",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_user_query_schema():
    """Return the generated Arrow schema for OCSF class 5018."""
    return _load_user_query_module().get_user_query_schema()


USER_QUERY_SCHEMA = get_user_query_schema()


@lru_cache(maxsize=1)
def _load_device_config_state_change_module() -> ModuleType:
    module_path = Path(__file__).with_name("5019_device_config_state_change.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5019_device_config_state_change",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_device_config_state_change_schema():
    """Return the generated Arrow schema for OCSF class 5019."""
    return _load_device_config_state_change_module().get_device_config_state_change_schema()


DEVICE_CONFIG_STATE_CHANGE_SCHEMA = get_device_config_state_change_schema()


@lru_cache(maxsize=1)
def _load_software_info_module() -> ModuleType:
    module_path = Path(__file__).with_name("5020_software_info.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.5_discovery._5020_software_info",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.5_discovery"
    spec.loader.exec_module(module)
    return module


def get_software_info_schema():
    """Return the generated Arrow schema for OCSF class 5020."""
    return _load_software_info_module().get_software_info_schema()


SOFTWARE_INFO_SCHEMA = get_software_info_schema()


__all__ = [
    "get_inventory_info_schema",
    "INVENTORY_INFO_SCHEMA",
    "get_config_state_schema",
    "CONFIG_STATE_SCHEMA",
    "get_user_inventory_schema",
    "USER_INVENTORY_SCHEMA",
    "get_patch_state_schema",
    "PATCH_STATE_SCHEMA",
    "get_kernel_object_query_schema",
    "KERNEL_OBJECT_QUERY_SCHEMA",
    "get_file_query_schema",
    "FILE_QUERY_SCHEMA",
    "get_folder_query_schema",
    "FOLDER_QUERY_SCHEMA",
    "get_admin_group_query_schema",
    "ADMIN_GROUP_QUERY_SCHEMA",
    "get_job_query_schema",
    "JOB_QUERY_SCHEMA",
    "get_module_query_schema",
    "MODULE_QUERY_SCHEMA",
    "get_network_connection_query_schema",
    "NETWORK_CONNECTION_QUERY_SCHEMA",
    "get_networks_query_schema",
    "NETWORKS_QUERY_SCHEMA",
    "get_peripheral_device_query_schema",
    "PERIPHERAL_DEVICE_QUERY_SCHEMA",
    "get_process_query_schema",
    "PROCESS_QUERY_SCHEMA",
    "get_service_query_schema",
    "SERVICE_QUERY_SCHEMA",
    "get_session_query_schema",
    "SESSION_QUERY_SCHEMA",
    "get_user_query_schema",
    "USER_QUERY_SCHEMA",
    "get_device_config_state_change_schema",
    "DEVICE_CONFIG_STATE_CHANGE_SCHEMA",
    "get_software_info_schema",
    "SOFTWARE_INFO_SCHEMA",
]
