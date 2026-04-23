import json
from dataclasses import asdict
from py_ocsf_arrow import SchemaGenerator


if __name__ == "__main__":
    # Example usage: generate and save Arrow schemas for all event classes in the default version
    class_name = "vulnerability_finding"
    generator = SchemaGenerator.init()
    print(generator.build_arrow_schema(class_name))
