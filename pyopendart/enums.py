from enum import Enum as BaseEnum


class Enum(BaseEnum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value


class Market(Enum):
    KOSPI = "Y"
    KOSDAQ = "K"
    KONEX = "N"
    ETC = "E"

    def __missing__(self, key):
        return None


class ReportType(Enum):
    Q1 = 11013  # 1분기보고서
    SEMI_ANNUAL = 11012  # 반기보고서
    Q3 = 11014  # 3분기보고서
    ANNUAL = 11011  # 사업보고서


class FinancialStatementDivision(Enum):
    FINANCIAL_STATEMENT = "OFS"
    CONSOLIDATED_FINANCIAL_STATEMENT = "CFS"


class FinancialStatementType(Enum):
    INCOME_STATEMENT = "IS"
    BALANCE_SHEET = "BS"
    COMPREHENSIVE_INCOME_STATEMENT = "CIS"
    CASH_FLOW = "CF"
    EQUITY_CHANGE_STATEMENT = "SCE"
