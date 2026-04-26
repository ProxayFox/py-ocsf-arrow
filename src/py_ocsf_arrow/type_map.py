"""Map OCSF scalar and derived types to PyArrow data types.

The :class:`TypeMapper` translates OCSF primitive types (e.g. ``boolean_t``,
``string_t``, ``long_t``) and schema-defined derived types into their corresponding
PyArrow scalar types. It builds and caches the complete type mapping for a given
OCSF schema version and is used as the shared type-resolution layer by schema
generation and other Arrow-backed operations.

This module provides :class:`TypeMapper` and the method :meth:`~TypeMapper.build_ocsf_to_arrow_mapping`
to construct or update the type mapping from schema metadata.
"""

import pyarrow as pa
from functools import cached_property
from typing import TypeAlias
from http.client import HTTPResponse
from urllib.response import addinfourl

# Local Imports
from . import OCSFArrow


class TypeMappingError(Exception):
    """Custom exception for type mapping errors."""

    pass


# Define a type alias for the response types we expect from urlopen
UrlopenResponse: TypeAlias = HTTPResponse | addinfourl


class TypeMapper(OCSFArrow):
    """Class to handle mapping between OCSF types and PyArrow types."""

    _BASE_OCSF_TYPES: dict[str, pa.DataType] = {
        "boolean_t": pa.bool8(),
        "float_t": pa.float32(),
        "integer_t": pa.int32(),
        "json_t": pa.string(),
        "long_t": pa.int64(),
        "string_t": pa.string(),
    }

    @cached_property
    def OCSF_TO_ARROW(self) -> dict[str, pa.DataType]:
        """Build and cache the OCSF to Arrow mapping for this instance."""
        return self.build_ocsf_to_arrow_mapping()

    def build_ocsf_to_arrow_mapping(self) -> dict[str, pa.DataType]:
        """Build the OCSF to Arrow mapping for this instance."""
        types = self.client.get_schema(version=self.version).types
        mapping: dict[str, pa.DataType] = self._BASE_OCSF_TYPES.copy()
        for type_name, type_info in types.items():
            if type_info.type_name is None or type_info.type is None:
                continue  # Skip base types as they're copied from _BASE_OCSF_TYPES

            if type_info.type in self._BASE_OCSF_TYPES.keys():
                mapping[type_name] = self._BASE_OCSF_TYPES[type_info.type]
            else:
                raise TypeMappingError(
                    f"Type {type_name} has unknown base type {type_info.type}"
                )
        return mapping
