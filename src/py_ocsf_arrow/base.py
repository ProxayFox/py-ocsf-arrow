from dataclasses import dataclass
from ocsf.api.client import OcsfApiClient

CLIENT = OcsfApiClient()


@dataclass
class OCSFArrow:
    """
    Base class for OCSF Arrow integration.
    """

    _base_url: str = CLIENT._base_url
    _data_type_endpoint: str = "/api/data_types"
