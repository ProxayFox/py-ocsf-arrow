import pytest
from ocsf.schema import OcsfSchema

from py_ocsf_arrow import TypeMapper


class TestTypeMapper:
    type_mapper = TypeMapper()

    def test_ocsf_base_mapping(self, ocsf_schemas: dict[str, OcsfSchema]):
        """Validate base-type mapping in both directions for every schema version.

        - BASE_OCSF_TYPES must match the union of all schema base types across
          supported versions (all possible base types).
        - Every version's base types must be mapped.
        """
        base_mapping = self.type_mapper.BASE_OCSF_TYPES
        mapped_base_types = set(base_mapping.keys())
        all_possible_base_types: set[str] = set()
        failures: list[str] = []

        for version, schema in ocsf_schemas.items():
            schema_base_types = {
                type_name
                for type_name, type_info in schema.types.items()
                if type_info.type_name is None
            }
            all_possible_base_types.update(schema_base_types)

            missing_from_mapping = schema_base_types - mapped_base_types

            if missing_from_mapping:
                failures.append(
                    f"Version {version}: missing base type mappings: "
                    f"{sorted(missing_from_mapping)}"
                )

            for type_name in schema_base_types:
                if type_name in base_mapping and base_mapping[type_name] is None:
                    failures.append(
                        f"Version {version}: base type {type_name} maps to None"
                    )

        extra_in_mapping = mapped_base_types - all_possible_base_types
        missing_from_mapping = all_possible_base_types - mapped_base_types

        if missing_from_mapping:
            failures.append(
                "BASE_OCSF_TYPES is missing possible base types across versions: "
                f"{sorted(missing_from_mapping)}"
            )
        if extra_in_mapping:
            failures.append(
                "BASE_OCSF_TYPES includes keys that are never base types in supported "
                f"versions: {sorted(extra_in_mapping)}"
            )

        if failures:
            pytest.fail("\n".join(failures))
