import requests
from furl import furl

from pyopendart import exceptions


class _DartSingleton(type):
    _clients = {}

    def __call__(cls, api_key: str):
        if api_key not in cls._clients:
            cls._clients[api_key] = super(_DartSingleton, cls).__call__(api_key)
        return cls._clients[api_key]


class DartClient(metaclass=_DartSingleton):
    dart_host = "https://opendart.fss.or.kr/api/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def json(self, name: str, **kwargs) -> dict:
        url = furl(self.dart_host)
        url /= f"{name}.json"
        url.args["crtfc_key"] = self.api_key
        url.args.update(kwargs)

        resp = requests.get(url.tostr())
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
