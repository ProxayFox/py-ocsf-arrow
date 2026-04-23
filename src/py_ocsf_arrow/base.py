from dataclasses import dataclass
from pathlib import Path
from ocsf.api.client import OcsfApiClient

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / ".cache"


@dataclass
class OCSFArrow:
    """
    Base class for OCSF Arrow integration.
    """

    client: OcsfApiClient
    version: str
    _base_url: str
    _data_type_endpoint: str = "/api/data_types"

    @classmethod
    def init(cls, version: str = "default", cache: bool | Path | str = True):
        """Factory method to create an instance of OCSFArrow with the API client."""
        match cache:
            case True:
                cache_path = CACHE_DIR
            case False:
                cache_path = None
            case str(_) | Path():
                cache_path = Path(cache)

        client = OcsfApiClient(cache_dir=cache_path)
        base_url = client._base_url
        if version == "default":
            version = client.get_default_version()
        elif version not in client.get_versions():
            raise ValueError(
                f"Version {version} is not supported by the OCSF API.")

        return cls(client=client, version=version, _base_url=base_url)
