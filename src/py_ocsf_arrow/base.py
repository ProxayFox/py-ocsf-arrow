from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from ocsf.api.client import OcsfApiClient
from ocsf.schema import OcsfSchema, OcsfExtension, OcsfProfile

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / ".cache"


@dataclass
class OCSFArrow:
    """Base class for OCSF Arrow integration."""

    client: OcsfApiClient
    version: str
    schema: OcsfSchema

    # List of extensions and profiles to ignore when generating schemas
    # Flipping the logic so we can just pop these from the schema instead of having to check for them in every method
    ext: list[str]
    prf: list[str]

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

        ext = _items(ext, schema.extensions, "Extension")
        prf = _items(prf, schema.profiles, "Profile")

        return cls(
            client=client, version=version, schema=schema, ext=ext or [], prf=prf or []
        )
