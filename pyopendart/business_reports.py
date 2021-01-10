from pyopendart.common import DartClient


class BusinessReports:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def capital_increases_and_decreases(self):
        pass

    def dividend(self):
        pass

    def treasury_shares_acquisition_and_disposition(self):
        pass

    def major_shareholders_status(self):
        pass

    def major_shareholders_changes(self):
        pass

    def minority_shareholders_status(self):
        pass

    def executives_status(self):
        pass

    def employees_status(self):
        pass

    def executives_individual_compensation_status(self):
        pass

    def executives_total_compensation_status(self):
        pass

    def individual_compensation_top_5(self):
        pass

    def investment_in_other_corporations(self):
        pass
