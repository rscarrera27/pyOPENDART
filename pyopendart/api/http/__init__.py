from abc import ABC, abstractmethod
from os import PathLike
from typing import Any, Dict, Generator, Mapping
from xml.etree import ElementTree

from pyopendart import exceptions

DartApiParamType = Dict[str, str]


def raise_for_dart_status(status: str, message: str) -> None:
    if status == "000":
        return

    exception = {
        "010": exceptions.UnregisteredKey,
        "011": exceptions.UnusableKey,
        "013": exceptions.Empty,
        "020": exceptions.RateLimited,
        "100": exceptions.InvalidParameter,
        "800": exceptions.UnderMaintenance,
    }.get(status, exceptions.UnknownError)(message)

    raise exception


class OpenApiClient(ABC):
    def __init__(
        self,
        api_key: str,
        default_timeout: Any = None,
        default_download_timeout: Any = None,
        use_connection_pool: bool = False,
    ):
        self.api_key = api_key
        self.default_timeout = default_timeout
        self.default_download_timeout = default_download_timeout
        self.use_connection_pool = use_connection_pool

    @abstractmethod
    def json_resource(self, resource: str, api_params: DartApiParamType, *, timeout: Any = None) -> Mapping:
        pass

    @abstractmethod
    def xml_resource(self, resource: str, api_params: DartApiParamType, *, timeout: Any = None) -> ElementTree:
        pass

    @abstractmethod
    def zip_resource(
        self, resource: str, api_params: DartApiParamType, extract_to: PathLike, *, timeout: Any = None
    ) -> None:
        pass

    @abstractmethod
    def iter_list_resource(
        self, resource: str, api_params: DartApiParamType, *, timeout: Any = None
    ) -> Generator[Dict[str, str], None, None]:
        pass
