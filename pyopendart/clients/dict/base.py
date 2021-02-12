from pyopendart.clients.http import DartClient


class DictClient:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)
