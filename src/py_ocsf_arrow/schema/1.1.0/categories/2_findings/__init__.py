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
def _load_security_finding_module() -> ModuleType:
    module_path = Path(__file__).with_name("2001_security_finding.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.2_findings._2001_security_finding",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.1.0.categories.2_findings"
    spec.loader.exec_module(module)
    return module


def get_security_finding_schema():
    """Return the generated Arrow schema for OCSF class 2001."""
    return _load_security_finding_module().get_security_finding_schema()


SECURITY_FINDING_SCHEMA = get_security_finding_schema()


@lru_cache(maxsize=1)
def _load_vulnerability_finding_module() -> ModuleType:
    module_path = Path(__file__).with_name("2002_vulnerability_finding.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.2_findings._2002_vulnerability_finding",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.1.0.categories.2_findings"
    spec.loader.exec_module(module)
    return module


def get_vulnerability_finding_schema():
    """Return the generated Arrow schema for OCSF class 2002."""
    return _load_vulnerability_finding_module().get_vulnerability_finding_schema()


VULNERABILITY_FINDING_SCHEMA = get_vulnerability_finding_schema()


@lru_cache(maxsize=1)
def _load_compliance_finding_module() -> ModuleType:
    module_path = Path(__file__).with_name("2003_compliance_finding.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.2_findings._2003_compliance_finding",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.1.0.categories.2_findings"
    spec.loader.exec_module(module)
    return module


def get_compliance_finding_schema():
    """Return the generated Arrow schema for OCSF class 2003."""
    return _load_compliance_finding_module().get_compliance_finding_schema()


COMPLIANCE_FINDING_SCHEMA = get_compliance_finding_schema()


@lru_cache(maxsize=1)
def _load_detection_finding_module() -> ModuleType:
    module_path = Path(__file__).with_name("2004_detection_finding.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.2_findings._2004_detection_finding",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.1.0.categories.2_findings"
    spec.loader.exec_module(module)
    return module


def get_detection_finding_schema():
    """Return the generated Arrow schema for OCSF class 2004."""
    return _load_detection_finding_module().get_detection_finding_schema()


DETECTION_FINDING_SCHEMA = get_detection_finding_schema()


@lru_cache(maxsize=1)
def _load_incident_finding_module() -> ModuleType:
    module_path = Path(__file__).with_name("2005_incident_finding.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.1.0.categories.2_findings._2005_incident_finding",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.1.0.categories.2_findings"
    spec.loader.exec_module(module)
    return module


def get_incident_finding_schema():
    """Return the generated Arrow schema for OCSF class 2005."""
    return _load_incident_finding_module().get_incident_finding_schema()


INCIDENT_FINDING_SCHEMA = get_incident_finding_schema()


__all__ = [
    "get_security_finding_schema",
    "SECURITY_FINDING_SCHEMA",
    "get_vulnerability_finding_schema",
    "VULNERABILITY_FINDING_SCHEMA",
    "get_compliance_finding_schema",
    "COMPLIANCE_FINDING_SCHEMA",
    "get_detection_finding_schema",
    "DETECTION_FINDING_SCHEMA",
    "get_incident_finding_schema",
    "INCIDENT_FINDING_SCHEMA",
]
