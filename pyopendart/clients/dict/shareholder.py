from pyopendart.client import DartClient


class Shares:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_major_shareholders(self):
        pass

    def get_executive_shareholders(self):
        pass
