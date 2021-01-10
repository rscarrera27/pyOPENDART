from dataclasses import dataclass
from datetime import date
from enum import Enum


@dataclass
class DateRange:
    begin: date  # bgn_de
    end: date  # end_de

    def serialize(self):
        return {"bgn_de": self.begin.strftime("%Y%m%d"), "end_de": self.end.strftime("%Y%m%d")}


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


class Market(Enum):
    KOSPI = "Y"
    KOSDAQ = "K"
    KONEX = "N"
    ETC = "E"

    def __missing__(self, key):
        return None
