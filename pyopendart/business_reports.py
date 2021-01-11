from pyopendart.client import DartClient


class BusinessReports:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_capital_variation(self):
        pass

    def get_dividend_info(self):
        pass

    def get_treasury_shares_status(self):
        pass

    def get_major_shareholders_status(self):
        pass

    def get_changes_in_major_shareholders(self):
        pass

    def get_minority_shareholders_status(self):
        pass

    def get_directors(self):
        pass

    def get_employee_status(self):
        pass

    def get_individual_executive_compensation_status(self):
        pass

    def get_executive_compensation_status(self):
        pass

    def get_top_5_individual_executive_compensation(self):
        pass

    def get_investment_in_other_corporations(self):
        pass
