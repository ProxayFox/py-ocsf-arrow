"""Provide the shared OCSF Arrow runtime foundation.

The :class:`OCSFArrow` base class manages the integration between the OCSF API
client and Arrow schema generation. It handles version selection, schema loading,
caching configuration, and the computation of which profile and extension attributes
to include or exclude when building schemas.

This module provides :class:`OCSFArrow` as a factory base (:meth:`~OCSFArrow.init`)
that higher-level schema generators and type mappers inherit from.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from ocsf.api.client import OcsfApiClient
from ocsf.schema import OcsfSchema

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / ".cache"


@dataclass
class OCSFArrow:
    """Base class for OCSF Arrow integration."""

    client: OcsfApiClient
    version: str
    schema: OcsfSchema

    # Keep track of which attributes to ignore based on the selected extensions and profiles
    _ignored_attr: set[str]

    @classmethod
    def init(
        cls,
        client: Optional[OcsfApiClient] = None,
        cache: Optional[bool | Path | str] = True,
        version: Optional[str] = "default",
        ext: list[str] | None = None,
        prf: list[str] | None = None,
    ):
        """Factory method to create an instance of OCSFArrow with the API client.

        Args:
            ext(list[str]): List of extension names to include when generating schemas.
            prf(list[str]): List of profile names to include when generating schemas.
            version(str): OCSF schema version to use (e.g. "1.0", "default", etc.)
            cache(bool | Path | str): Whether to cache API responses, or a path to use for caching.

        returns:
            An instance of OCSFArrow with the client and schema loaded.
        """

        # Helper functions for validating and processing extensions and profiles
        def _items(
            items: list[str] | None, schema_items: dict | None, item_type: str
        ) -> list[str]:
            """Helper function to validate provided items against the schema and return the list of items to ignore."""
            if schema_items is None:
                raise ValueError(
                    f"Schema version {version} does not include any {item_type.lower()}s, but {item_type}(s) were provided."
                )
            # If no items provided, ignore all
            if items is None:
                return [name for name in schema_items.keys()]

            # Validate provided items and return the list of items to ignore
            invalid_items = [item for item in items if item not in schema_items]
            if invalid_items:
                raise ValueError(
                    f"{item_type}(s) {invalid_items} not found in schema version {version}"
                )

            # Ignore any items not in the provided list
            return [name for name in schema_items.keys() if name not in items]

        cache_path: Optional[Path] = None
        match cache:
            case True:
                cache_path = CACHE_DIR
            case False:
                cache_path = None
            case str(_) | Path():
                cache_path = Path(cache)

        client = OcsfApiClient(cache_dir=cache_path) if client is None else client
        if version == "default":
            version = client.get_default_version()
        elif version not in client.get_versions():
            raise ValueError(f"Version {version} is not supported by the OCSF API.")
        schema = client.get_schema(version=version)

        if schema.profiles is None or schema.extensions is None:
            raise ValueError(
                f"Schema version {version} must include both profiles and extensions."
            )

        ext = _items(ext, schema.extensions, "Extension")
        prf = _items(prf, schema.profiles, "Profile")

        ext_profiles: list[str] = []
        for ext_name in ext:
            match ext_name:
                case "linux":
                    ext_profiles.append("linux/linux_users")
                case "macos":
                    ext_profiles.append("macos/macos_users")
                case "win":
                    # No user-related attributes in the Windows extension, so we can skip it entirely
                    continue
                case _:
                    ext_profiles.append(ext_name)

        prf.extend(ext_profiles)
        attr: set[str] = set()

        for name in prf:
            attr_expand = schema.profiles[name].attributes.keys()
            attr.update(attr_expand)

        return cls(client=client, version=version, schema=schema, _ignored_attr=attr)
