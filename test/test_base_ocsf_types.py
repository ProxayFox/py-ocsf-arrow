import pytest
from ocsf.schema import OcsfSchema

from py_ocsf_arrow import TypeMapper


class TestTypeMapper:
    type_mapper = TypeMapper.init(version="default")

    def test_ocsf_base_mapping(self, ocsf_schemas: dict[str, OcsfSchema]):
        """Validate base-type mapping in both directions for every schema version.

        - BASE_OCSF_TYPES must match the union of all schema base types across
          supported versions (all possible base types).
        - Every version's base types must be mapped.
        """
        base_mapping = self.type_mapper._BASE_OCSF_TYPES
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

    def test_ocsf_to_arrow_mapping_complete(self, ocsf_schemas: dict[str, OcsfSchema]):
        """Validate that OCSF_TO_ARROW mapping is complete and correct.

        - All base types must be present in the mapping.
        - All mapped types must have non-None Arrow types.
        - All derived types must map to a valid base type that exists in the mapping.
        """
        ocsf_to_arrow = self.type_mapper.OCSF_TO_ARROW
        base_mapping = self.type_mapper._BASE_OCSF_TYPES
        failures: list[str] = []

        # Verify all base types are in the mapping
        for base_type_name in base_mapping.keys():
            if base_type_name not in ocsf_to_arrow:
                failures.append(
                    f"Base type {base_type_name} missing from OCSF_TO_ARROW")

        # Verify no None values in mapping
        for type_name, arrow_type in ocsf_to_arrow.items():
            if arrow_type is None:
                failures.append(f"Type {type_name} maps to None")

        # Verify mapping is consistent: derived types should map to the same
        # Arrow type as their base type
        for version, schema in ocsf_schemas.items():
            for type_name, type_info in schema.types.items():
                # Skip base types (type_name is None when it's a base type)
                if type_info.type_name is None or type_info.type is None:
                    continue

                if type_name not in ocsf_to_arrow:
                    failures.append(
                        f"Version {version}: derived type {type_name} not in OCSF_TO_ARROW"
                    )
                elif type_info.type not in ocsf_to_arrow:
                    failures.append(
                        f"Version {version}: base type {type_info.type} "
                        f"for derived {type_name} not in OCSF_TO_ARROW"
                    )
                else:
                    # Verify the derived type maps to the same Arrow type as its base
                    derived_arrow = ocsf_to_arrow[type_name]
                    base_arrow = ocsf_to_arrow[type_info.type]
                    if derived_arrow != base_arrow:
                        failures.append(
                            f"Version {version}: {type_name} maps to {derived_arrow} "
                            f"but its base type {type_info.type} maps to {base_arrow}"
                        )

        if failures:
            pytest.fail("\n".join(failures))
