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


class SortBy(Enum):
    DATE = "date"
    CORP_NAME = "crp"
    REPORT_NAME = "rpt"


class DisclosureType(Enum):
    A = "A"  # 정기공시
    B = "B"  # 주요사항보고
    C = "C"  # 발행공시
    D = "D"  # 지분공시
    E = "E"  # 기타공시
    F = "F"  # 외부감사관련
    G = "G"  # 펀드공시
    H = "H"  # 자산유동화
    I = "I"  # 거래소공시
    J = "J"  # 공정위공시
