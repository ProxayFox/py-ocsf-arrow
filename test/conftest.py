import pytest
from pathlib import Path

from ocsf.api.client import OcsfApiClient
from ocsf.util import get_schema
from ocsf.schema import OcsfSchema


REPO_ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = REPO_ROOT / ".cache"
OUTPUT_DIR = REPO_ROOT / "outputs"


@pytest.fixture(scope="session")
def ocsf_client() -> OcsfApiClient:
    """Create a single OcsfApiClient instance for the test session."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OcsfApiClient(cache_dir=CACHE_DIR)


@pytest.fixture(scope="session")
def ocsf_versions(ocsf_client: OcsfApiClient) -> list[str]:
    """Get the list of OCSF schema versions to test against, excluding pre-releases."""
    return [
        version
        for version in ocsf_client.get_versions()
        if "-rc" not in version and "-dev" not in version
    ]


@pytest.fixture(scope="session")
def ocsf_schemas(
    ocsf_client: OcsfApiClient, ocsf_versions: list[str]
) -> dict[str, OcsfSchema]:
    """Get the OCSF schemas for the specified versions."""
    return {version: get_schema(version, ocsf_client) for version in ocsf_versions}
