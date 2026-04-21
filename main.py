from ocsf.api.client import OcsfApiClient

from py_ocsf_arrow.schema_gen import build_arrow_schema

# Load OCSF schema v1.8.0 (from API, file, or repo)
client = OcsfApiClient()

ocsf_old_schema = client.get_schema("1.7.0")
print("OCSF schema loaded successfully" if ocsf_old_schema is not None else "Failed to load OCSF schema")


ocsf_version = client.get_default_version()
ocsf_schema = client.get_schema(ocsf_version)

print("OCSF schema loaded successfully" if ocsf_schema is not None else "Failed to load OCSF schema")
exit()

# Generate Arrow schema for Vulnerability Finding (class 2002)
vuln_finding_schema = build_arrow_schema(ocsf_schema, "vulnerability_finding")

print(vuln_finding_schema)
# activity_id: int32 not null
# activity_name: string
# severity_id: int32 not null
# severity: string
# finding_info: string          ← object types flatten to JSON string
# ...
