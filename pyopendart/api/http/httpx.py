from io import BytesIO
from os import PathLike
from tempfile import TemporaryFile
from typing import Any, Dict, Generator, Mapping, Optional
from xml.etree import ElementTree
from zipfile import ZipFile

from furl import furl

try:
    import httpx
except ImportError:
    httpx = False

from pyopendart.api.http import DartApiParamType, OpenApiClient, raise_for_dart_status


class HttpxOpenApiClient(OpenApiClient):
    def __init__(
        self,
        api_key: str,
        default_timeout: Any = None,
        default_download_timeout: Any = None,
        use_connection_pool: bool = False,
    ):
        if httpx is False:
            # fmt: off
            raise ImportError(
                'Cannot find module "httpx". Please install "httpx" extras.\n'
                '\n'
                '> $ pip install pyopendart[httpx]'
            )
            # fmt: on

        super().__init__(api_key, default_timeout, default_download_timeout, use_connection_pool)
        self._session: Optional["httpx.Client"] = None
        self._dart_openapi_base_url = "https://opendart.fss.or.kr/api/"

    def _get_session(self) -> "httpx.Client":
        if self._session is not None:
            return self._session
        self._session = httpx.Client()
        return self._session

    def _get_client(self) -> "httpx.Client":
        if self.use_connection_pool:
            return self._get_session()
        return httpx.Client()

    def json_resource(self, resource: str, api_params: DartApiParamType, *, timeout: Any = None) -> Mapping:
        url = furl(self._dart_openapi_base_url + f"{resource}.json")
        url.args.update({"crtfc_key": self.api_key, **api_params})
        timeout = timeout or self.default_timeout

        res = self._get_client().get(url.tostr(), timeout=timeout)
        res.raise_for_status()
        json = res.json()

        raise_for_dart_status(json.get("status"), json.get("message"))

        del json["status"]
        del json["message"]

        return json

    def xml_resource(self, resource: str, api_params: DartApiParamType, *, timeout: Any = None) -> ElementTree:
        url = furl(self._dart_openapi_base_url + f"{resource}.xml")
        url.args.update({"crtfc_key": self.api_key, **api_params})
        timeout = timeout or self.default_timeout

        res = self._get_client().get(url.tostr(), timeout=timeout)
        res.raise_for_status()
        etree = ElementTree.parse(BytesIO(res.content))

        status_element = etree.find("status")
        message_element = etree.find("message")

        raise_for_dart_status(status_element.text, message_element.text)

        etree.getroot().remove(status_element)
        etree.getroot().remove(message_element)

        return etree

    def zip_resource(
        self, resource: str, api_params: DartApiParamType, extract_to: PathLike, *, timeout: Any = None
    ) -> None:
        url = furl(self._dart_openapi_base_url + f"{resource}.xml")
        url.args.update({"crtfc_key": self.api_key, **api_params})
        timeout = timeout or self.default_timeout

        res = self._get_client().get(url.tostr(), timeout=timeout)
        res.raise_for_status()

        content_type = res.headers.get("Content-Type")
        if content_type == "application/xml" or res.headers.get("Content-Disposition") is None:
            etree = ElementTree.parse(BytesIO(res.content))
            raise_for_dart_status(etree.find("status").text, etree.find("message").text)

        with TemporaryFile() as tempf:
            for chunk in res.iter_bytes():
                if chunk is not None:
                    tempf.write(chunk)

            with ZipFile(tempf) as zipf:
                zipf.extractall(extract_to)

    def iter_list_resource(
        self, resource: str, api_params: DartApiParamType, *, timeout: Any = None
    ) -> Generator[Dict[str, str], None, None]:
        etree = self.xml_resource(resource, api_params, timeout=timeout)

        for item in etree.iter("list"):
            yield {element.tag: element.text for element in item}
