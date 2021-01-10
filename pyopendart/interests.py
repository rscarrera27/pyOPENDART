from pyopendart.common import DartClient


class DisclosureOfInterests:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def major_shareholders_report(self):
        pass

    def executive_shareholders_report(self):
        pass
