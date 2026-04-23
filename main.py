import json
from pathlib import Path
from ocsf.api.client import OcsfApiClient
from ocsf.util import get_schema
from dataclasses import asdict
from typing import Any

CACHE_DIR = Path(".cache")
if not CACHE_DIR.exists():
    CACHE_DIR.mkdir(parents=True)

OUTPUT_DIR = Path("outputs")
if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir(parents=True)

CLIENT = OcsfApiClient(cache_dir=CACHE_DIR)


def ocsf_types(ocsf_version: str) -> list[dict[str, Any]]:
    ocsf_schema = get_schema(ocsf_version, CLIENT)

    types: list[dict[str, Any]] = []
    for type_name, type_info in ocsf_schema.types.items():
        type: dict[str, Any] = {"name": type_name}
        type.update(asdict(type_info))
        types.append(type)

    return types


if __name__ == "__main__":
    versions = CLIENT.get_versions()
    files: list[dict[str, str]] = []

    for version in versions:
        print(f"Processing OCSF version {version}...")
        file = OUTPUT_DIR / f"ocsf_types_{version}.json"
        files.append({"version": version, "file": file.as_posix()})

        with open(file, "w") as f:
            json.dump(ocsf_types(version), f, indent=4)

    if all(Path(file["file"]).exists() for file in files) and len(files) == len(
        versions
    ):
        print("All files created successfully.")
    else:
        print("Error: One or more files were not created.")
