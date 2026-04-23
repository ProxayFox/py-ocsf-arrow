import pyarrow as pa
import json
from functools import cached_property
from typing import TypeAlias, cast
from http.client import HTTPResponse
from urllib.parse import urljoin
from urllib.request import urlopen
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

    BASE_OCSF_TYPES: dict[str, pa.DataType] = {
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
        """Fetch the OCSF data types from the API and build the mapping."""
        ocsf_types: dict[str, dict] = self.get_data_type()
        mapping = self.BASE_OCSF_TYPES.copy()  # Start with the base types
        for ocsf_type in ocsf_types:
            if ocsf_type in self.BASE_OCSF_TYPES:
                continue  # Use the predefined mapping for base types

            base_type = ocsf_types[ocsf_type].get("type")
            if base_type in self.BASE_OCSF_TYPES:
                mapping[ocsf_type] = self.BASE_OCSF_TYPES[base_type]
            else:
                raise TypeMappingError(f"Unsupported OCSF type: {ocsf_type}")

        return mapping

    def get_data_type(self) -> dict[str, dict]:
        """Get the OCSF Datatypes from the API and Cache them."""
        url = urljoin(self._base_url, self._data_type_endpoint)

        with cast(UrlopenResponse, urlopen(url)) as response:
            data_types = response.read()

        return json.loads(data_types)
