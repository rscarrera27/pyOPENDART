from pyopendart.client import DartClient


class DisclosureOfInterests:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_major_shares_report(self):
        pass

    def get_executive_shareholders_report(self):
        pass
