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
def _load_network_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4001_network_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4001_network_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_network_activity_schema():
    """Return the generated Arrow schema for OCSF class 4001."""
    return _load_network_activity_module().get_network_activity_schema()


NETWORK_ACTIVITY_SCHEMA = get_network_activity_schema()


@lru_cache(maxsize=1)
def _load_http_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4002_http_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4002_http_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_http_activity_schema():
    """Return the generated Arrow schema for OCSF class 4002."""
    return _load_http_activity_module().get_http_activity_schema()


HTTP_ACTIVITY_SCHEMA = get_http_activity_schema()


@lru_cache(maxsize=1)
def _load_dns_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4003_dns_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4003_dns_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_dns_activity_schema():
    """Return the generated Arrow schema for OCSF class 4003."""
    return _load_dns_activity_module().get_dns_activity_schema()


DNS_ACTIVITY_SCHEMA = get_dns_activity_schema()


@lru_cache(maxsize=1)
def _load_dhcp_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4004_dhcp_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4004_dhcp_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_dhcp_activity_schema():
    """Return the generated Arrow schema for OCSF class 4004."""
    return _load_dhcp_activity_module().get_dhcp_activity_schema()


DHCP_ACTIVITY_SCHEMA = get_dhcp_activity_schema()


@lru_cache(maxsize=1)
def _load_rdp_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4005_rdp_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4005_rdp_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_rdp_activity_schema():
    """Return the generated Arrow schema for OCSF class 4005."""
    return _load_rdp_activity_module().get_rdp_activity_schema()


RDP_ACTIVITY_SCHEMA = get_rdp_activity_schema()


@lru_cache(maxsize=1)
def _load_smb_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4006_smb_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4006_smb_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_smb_activity_schema():
    """Return the generated Arrow schema for OCSF class 4006."""
    return _load_smb_activity_module().get_smb_activity_schema()


SMB_ACTIVITY_SCHEMA = get_smb_activity_schema()


@lru_cache(maxsize=1)
def _load_ssh_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4007_ssh_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4007_ssh_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_ssh_activity_schema():
    """Return the generated Arrow schema for OCSF class 4007."""
    return _load_ssh_activity_module().get_ssh_activity_schema()


SSH_ACTIVITY_SCHEMA = get_ssh_activity_schema()


@lru_cache(maxsize=1)
def _load_ftp_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4008_ftp_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4008_ftp_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_ftp_activity_schema():
    """Return the generated Arrow schema for OCSF class 4008."""
    return _load_ftp_activity_module().get_ftp_activity_schema()


FTP_ACTIVITY_SCHEMA = get_ftp_activity_schema()


@lru_cache(maxsize=1)
def _load_email_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4009_email_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4009_email_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_email_activity_schema():
    """Return the generated Arrow schema for OCSF class 4009."""
    return _load_email_activity_module().get_email_activity_schema()


EMAIL_ACTIVITY_SCHEMA = get_email_activity_schema()


@lru_cache(maxsize=1)
def _load_network_file_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4010_network_file_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4010_network_file_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_network_file_activity_schema():
    """Return the generated Arrow schema for OCSF class 4010."""
    return _load_network_file_activity_module().get_network_file_activity_schema()


NETWORK_FILE_ACTIVITY_SCHEMA = get_network_file_activity_schema()


@lru_cache(maxsize=1)
def _load_email_file_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4011_email_file_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4011_email_file_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_email_file_activity_schema():
    """Return the generated Arrow schema for OCSF class 4011."""
    return _load_email_file_activity_module().get_email_file_activity_schema()


EMAIL_FILE_ACTIVITY_SCHEMA = get_email_file_activity_schema()


@lru_cache(maxsize=1)
def _load_email_url_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4012_email_url_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4012_email_url_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_email_url_activity_schema():
    """Return the generated Arrow schema for OCSF class 4012."""
    return _load_email_url_activity_module().get_email_url_activity_schema()


EMAIL_URL_ACTIVITY_SCHEMA = get_email_url_activity_schema()


@lru_cache(maxsize=1)
def _load_ntp_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4013_ntp_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4013_ntp_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_ntp_activity_schema():
    """Return the generated Arrow schema for OCSF class 4013."""
    return _load_ntp_activity_module().get_ntp_activity_schema()


NTP_ACTIVITY_SCHEMA = get_ntp_activity_schema()


@lru_cache(maxsize=1)
def _load_tunnel_activity_module() -> ModuleType:
    module_path = Path(__file__).with_name("4014_tunnel_activity.py")
    spec = spec_from_file_location(
        "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity._4014_tunnel_activity",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load schema module from {module_path}")
    module = module_from_spec(spec)
    module.__package__ = "py_ocsf_arrow.schema.1.3.0.categories.4_network_activity"
    spec.loader.exec_module(module)
    return module


def get_tunnel_activity_schema():
    """Return the generated Arrow schema for OCSF class 4014."""
    return _load_tunnel_activity_module().get_tunnel_activity_schema()


TUNNEL_ACTIVITY_SCHEMA = get_tunnel_activity_schema()


__all__ = [
    "get_network_activity_schema",
    "NETWORK_ACTIVITY_SCHEMA",
    "get_http_activity_schema",
    "HTTP_ACTIVITY_SCHEMA",
    "get_dns_activity_schema",
    "DNS_ACTIVITY_SCHEMA",
    "get_dhcp_activity_schema",
    "DHCP_ACTIVITY_SCHEMA",
    "get_rdp_activity_schema",
    "RDP_ACTIVITY_SCHEMA",
    "get_smb_activity_schema",
    "SMB_ACTIVITY_SCHEMA",
    "get_ssh_activity_schema",
    "SSH_ACTIVITY_SCHEMA",
    "get_ftp_activity_schema",
    "FTP_ACTIVITY_SCHEMA",
    "get_email_activity_schema",
    "EMAIL_ACTIVITY_SCHEMA",
    "get_network_file_activity_schema",
    "NETWORK_FILE_ACTIVITY_SCHEMA",
    "get_email_file_activity_schema",
    "EMAIL_FILE_ACTIVITY_SCHEMA",
    "get_email_url_activity_schema",
    "EMAIL_URL_ACTIVITY_SCHEMA",
    "get_ntp_activity_schema",
    "NTP_ACTIVITY_SCHEMA",
    "get_tunnel_activity_schema",
    "TUNNEL_ACTIVITY_SCHEMA",
]
