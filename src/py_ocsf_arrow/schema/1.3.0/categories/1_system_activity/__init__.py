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
def _load_file_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1001_file_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1001_file_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_file_activity_schema():
    """Return the generated Arrow schema for OCSF class 1001."""
    return _load_file_activity_module().get_file_activity_schema()


FILE_ACTIVITY_SCHEMA = get_file_activity_schema()


@lru_cache(maxsize=1)
def _load_kernel_extension_module() -> ModuleType:
    module_path = Path(__file__).with_name("1002_kernel_extension.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1002_kernel_extension",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_kernel_extension_schema():
    """Return the generated Arrow schema for OCSF class 1002."""
    return _load_kernel_extension_module().get_kernel_extension_schema()


KERNEL_EXTENSION_SCHEMA = get_kernel_extension_schema()


@lru_cache(maxsize=1)
def _load_kernel_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1003_kernel_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1003_kernel_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_kernel_activity_schema():
    """Return the generated Arrow schema for OCSF class 1003."""
    return _load_kernel_activity_module().get_kernel_activity_schema()


KERNEL_ACTIVITY_SCHEMA = get_kernel_activity_schema()


@lru_cache(maxsize=1)
def _load_memory_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1004_memory_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1004_memory_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_memory_activity_schema():
    """Return the generated Arrow schema for OCSF class 1004."""
    return _load_memory_activity_module().get_memory_activity_schema()


MEMORY_ACTIVITY_SCHEMA = get_memory_activity_schema()


@lru_cache(maxsize=1)
def _load_module_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1005_module_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1005_module_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_module_activity_schema():
    """Return the generated Arrow schema for OCSF class 1005."""
    return _load_module_activity_module().get_module_activity_schema()


MODULE_ACTIVITY_SCHEMA = get_module_activity_schema()


@lru_cache(maxsize=1)
def _load_scheduled_job_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1006_scheduled_job_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1006_scheduled_job_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_scheduled_job_activity_schema():
    """Return the generated Arrow schema for OCSF class 1006."""
    return _load_scheduled_job_activity_module().get_scheduled_job_activity_schema()


SCHEDULED_JOB_ACTIVITY_SCHEMA = get_scheduled_job_activity_schema()


@lru_cache(maxsize=1)
def _load_process_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("1007_process_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1007_process_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_process_activity_schema():
    """Return the generated Arrow schema for OCSF class 1007."""
    return _load_process_activity_module().get_process_activity_schema()


PROCESS_ACTIVITY_SCHEMA = get_process_activity_schema()


@lru_cache(maxsize=1)
def _load_event_log_module() -> ModuleType:
    module_path = Path(__file__).with_name("1008_event_log.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity._1008_event_log",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.1_system_activity"
    spec.loader.exec_module(module)
    return module


def get_event_log_schema():
    """Return the generated Arrow schema for OCSF class 1008."""
    return _load_event_log_module().get_event_log_schema()


EVENT_LOG_SCHEMA = get_event_log_schema()


__all__ = [
    "get_file_activity_schema",
    "FILE_ACTIVITY_SCHEMA",
    "get_kernel_extension_schema",
    "KERNEL_EXTENSION_SCHEMA",
    "get_kernel_activity_schema",
    "KERNEL_ACTIVITY_SCHEMA",
    "get_memory_activity_schema",
    "MEMORY_ACTIVITY_SCHEMA",
    "get_module_activity_schema",
    "MODULE_ACTIVITY_SCHEMA",
    "get_scheduled_job_activity_schema",
    "SCHEDULED_JOB_ACTIVITY_SCHEMA",
    "get_process_activity_schema",
    "PROCESS_ACTIVITY_SCHEMA",
    "get_event_log_schema",
    "EVENT_LOG_SCHEMA",
]
