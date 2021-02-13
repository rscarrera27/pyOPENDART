from abc import ABC, abstractmethod
from tempfile import TemporaryFile
from typing import Any
from zipfile import ZipFile

import requests
import xmltodict
from furl import furl

from pyopendart import exceptions

try:
    import httpx
except ImportError:
    httpx = False


class OpenApiClient(ABC):
    def __init__(
        self, api_key: str, default_timeout: Any = None, default_download_timeout: Any = None, **kwargs
    ) -> None:
        self.api_key = api_key
        self.default_timeout = default_timeout
        self.default_download_timeout = default_download_timeout

    @abstractmethod
    def json(self, name: str, params: dict, timeout: Any = None) -> dict:
        pass

    @abstractmethod
    def xml(self, name: str, params: dict, timeout: Any = None) -> dict:
        pass

    @abstractmethod
    def download(self, name: str, params: dict, save_to: str, timeout: Any = None, **kwargs) -> str:
        pass


class RequestsOpenApiClient(OpenApiClient):
    dart_host = "https://opendart.fss.or.kr/api/"

    def json(self, name: str, params: dict, timeout: Any = None) -> dict:
        url = furl(self.dart_host)
        url /= f"{name}.json"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_timeout

        resp = requests.get(url.tostr(), timeout=timeout)
        json = resp.json()

        if json.get("status") != "000":
            status = json.get("status")
            message = json.get("message")

            exception = {
                "010": exceptions.UnregisteredKey,
                "011": exceptions.UnusableKey,
                "013": exceptions.Empty,
                "020": exceptions.RateLimited,
                "100": exceptions.InvalidParameter,
                "800": exceptions.UnderMaintenance,
            }.get(status, exceptions.UnknownError)(message)

            raise exception

        del json["status"]
        del json["message"]

        return json

    def xml(self, name: str, params: dict, timeout: Any = None) -> dict:
        url = furl(self.dart_host)
        url /= f"{name}.xml"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_timeout

        resp = requests.get(url.tostr(), timeout=timeout)
        xml = xmltodict.parse(resp.content).get("result", {})

        if xml.get("status") != "000":
            status = xml.get("status")
            message = xml.get("message")

            exception = {
                "010": exceptions.UnregisteredKey,
                "011": exceptions.UnusableKey,
                "013": exceptions.Empty,
                "020": exceptions.RateLimited,
                "100": exceptions.InvalidParameter,
                "800": exceptions.UnderMaintenance,
            }.get(status, exceptions.UnknownError)(message)

            raise exception

        del xml["status"]
        del xml["message"]

        if xml.get("list") and isinstance(xml.get("list"), dict):
            xml["list"] = [xml.get("list")]

        return xml

    def download(self, name: str, params: dict, save_to: str, timeout: Any = None, **kwargs) -> str:
        url = furl(self.dart_host)
        url /= f"{name}.xml"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_download_timeout

        resp = requests.get(url.tostr(), timeout=timeout)

        cont_disp = resp.headers.get("Content-Disposition")
        if not cont_disp or "attachment" not in cont_disp:
            raise exceptions.Empty("Empty download response")

        with TemporaryFile(prefix="pyopendart_download") as tempf:
            for chunk in resp.iter_content(chunk_size=64 * 1024):
                if chunk is not None:
                    tempf.write(chunk)

            with ZipFile(tempf) as zipf:
                zipf.extractall(save_to)

        return save_to


class HttpxOpenApiClient(OpenApiClient):
    dart_host = "https://opendart.fss.or.kr/api/"

    def __init__(
        self, api_key: str, default_timeout: Any = None, default_download_timeout: Any = None, **kwargs
    ) -> None:
        if httpx is False:
            raise ImportError("httpx not installed")

        super(HttpxOpenApiClient, self).__init__(api_key, default_timeout, default_download_timeout, **kwargs)

    def json(self, name: str, params: dict, timeout: Any = None) -> dict:
        url = furl(self.dart_host)
        url /= f"{name}.json"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_timeout

        resp = httpx.get(url.tostr(), timeout=timeout)
        json = resp.json()

        if json.get("status") != "000":
            status = json.get("status")
            message = json.get("message")

            exception = {
                "010": exceptions.UnregisteredKey,
                "011": exceptions.UnusableKey,
                "013": exceptions.Empty,
                "020": exceptions.RateLimited,
                "100": exceptions.InvalidParameter,
                "800": exceptions.UnderMaintenance,
            }.get(status, exceptions.UnknownError)(message)

            raise exception

        del json["status"]
        del json["message"]

        return json

    def xml(self, name: str, params: dict, timeout: Any = None) -> dict:
        url = furl(self.dart_host)
        url /= f"{name}.xml"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_timeout

        resp = requests.get(url.tostr(), timeout=timeout)
        xml = xmltodict.parse(resp.content).get("result", {})

        if xml.get("status") != "000":
            status = xml.get("status")
            message = xml.get("message")

            exception = {
                "010": exceptions.UnregisteredKey,
                "011": exceptions.UnusableKey,
                "013": exceptions.Empty,
                "020": exceptions.RateLimited,
                "100": exceptions.InvalidParameter,
                "800": exceptions.UnderMaintenance,
            }.get(status, exceptions.UnknownError)(message)

            raise exception

        del xml["status"]
        del xml["message"]

        if xml.get("list") and isinstance(xml.get("list"), dict):
            xml["list"] = [xml.get("list")]

        return xml

    def download(self, name: str, params: dict, save_to: str, timeout: Any = None, **kwargs) -> str:
        url = furl(self.dart_host)
        url /= f"{name}.xml"
        url.args["crtfc_key"] = self.api_key
        url.args.update(params)

        timeout = timeout or self.default_download_timeout

        resp = httpx.get(url.tostr(), timeout=timeout)

        cont_disp = resp.headers.get("Content-Disposition")
        if not cont_disp or "attachment" not in cont_disp:
            raise exceptions.Empty("Empty download response")

        with TemporaryFile(prefix="pyopendart_download") as tempf:
            for chunk in resp.iter_bytes():
                if chunk is not None:
                    tempf.write(chunk)

            with ZipFile(tempf) as zipf:
                zipf.extractall(save_to)

        return save_to
