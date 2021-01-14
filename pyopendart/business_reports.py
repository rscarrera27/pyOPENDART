import locale
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional, Tuple, Union

from dateutil.parser import parse as datetime_parse

from pyopendart.client import DartClient
from pyopendart.common import Market


class ReportCode(Enum):
    Q1 = 11013  # 1분기보고서
    Q2 = 11012  # 반기보고서
    Q3 = 11014  # 3분기보고서
    Q4 = 11011  # 사업보고서


def dart_atoi(a: str) -> Union[int, float]:
    try:
        return int(a.replace(",", ""))
    except ValueError:
        return float(a.replace(",", ""))


@dataclass(frozen=True)
class BusinessReportItemBase:
    receipt_no: str  # rcept_no
    market: Market  # corp_cls
    corporation_code: str  # corp_code
    corporation_name: str  # corp_name


@dataclass(frozen=True)
class CapitalVariation(BusinessReportItemBase):
    date: date  # stock_isu_dcrs_de
    title: str  # isu_dcrs_stle
    stock_type: str  # isu_dcrs_stock_knd
    quantity: int  # isu_dcrs_qy
    face_value: int  # isu_dcrs_mstvdv_fval_amount
    issue_price: int  # isu_dcrs_mstvdv_amount

    @staticmethod
    def from_dart_resp(resp):
        return CapitalVariation(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            date=datetime_parse(resp["stock_isu_dcrs_de"]) if resp.get("stock_isu_dcrs_de") else None,
            title=resp.get("isu_dcrs_stle"),
            stock_type=resp.get("isu_dcrs_stock_knd"),
            quantity=dart_atoi(resp.get("isu_dcrs_qy")),
            face_value=dart_atoi(resp.get("isu_dcrs_mstvdv_fval_amount")),
            issue_price=dart_atoi(resp.get("isu_dcrs_mstvdv_amount")),
        )


@dataclass(frozen=True)
class DividendInfo(BusinessReportItemBase):
    title: str  # se
    stock_type: Optional[str]  # stock_knd
    current_term: Union[int, float]  # thstrm
    prev_term: Union[int, float]  # frmtrm
    prev_prev_term: Union[int, float]  # lwfr

    @staticmethod
    def from_dart_resp(resp):
        return DividendInfo(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            title=resp.get("se"),
            stock_type=resp.get("stock_knd"),
            current_term=dart_atoi(resp.get("thstrm")),
            prev_term=dart_atoi(resp.get("frmtrm")),
            prev_prev_term=dart_atoi(resp.get("lwfr")),
        )


@dataclass(frozen=True)
class TreasurySharesStatus(BusinessReportItemBase):
    stock_type: str  # stock_knd
    acquisition_methods: Tuple[str, str, str]  # acqs_mth1, acqs_mth2, acqs_mth3
    quantity_term_start: Optional[int]  # bsis_qy
    acquired: Optional[int]  # change_qy_acqs
    disposed: Optional[int]  # change_qy_dsps
    retired: Optional[int]  # change_qy_incnr
    quantity_term_end: Optional[int]  # trmend_qy
    remarks: str  # rm

    @staticmethod
    def from_dart_resp(resp):
        return TreasurySharesStatus(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            stock_type=resp.get("stock_knd"),
            acquisition_methods=(
                resp.get("acqs_mth1"),
                resp.get("acqs_mth2"),
                resp.get("acqs_mth3"),
            ),
            quantity_term_start=dart_atoi(resp.get("bsis_qy")),
            acquired=dart_atoi(resp.get("change_qy_acqs")),
            disposed=dart_atoi(resp.get("change_qy_dsps")),
            retired=dart_atoi(resp.get("change_qy_incnr")),
            quantity_term_end=dart_atoi(resp.get("trmend_qy")),
            remarks=resp.get("rm"),
        )


@dataclass(frozen=True)
class MajorShareholder(BusinessReportItemBase):
    name: str  # nm
    relation: str  # relate
    stock_type: str  # stock_knd

    @dataclass(frozen=True)
    class QuantityAndShareholdingRatio:
        quantity: int
        shareholding_ratio: float

    term_start: QuantityAndShareholdingRatio  # bsis_posesn_stock_co, bsis_posesn_stock_qota_rt
    term_end: QuantityAndShareholdingRatio  # trmend_posesn_stock_co, trmend_posesn_stock_qota_rt
    remarks: str  # rm

    @staticmethod
    def from_dart_resp(resp):
        return MajorShareholder(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            name=resp.get("nm"),
            relation=resp.get("relate"),
            stock_type=resp.get("stock_knd"),
            term_start=MajorShareholder.QuantityAndShareholdingRatio(
                quantity=dart_atoi(resp.get("bsis_posesn_stock_co")),
                shareholding_ratio=dart_atoi(resp.get("bsis_posesn_stock_qota_rt")),
            ),
            term_end=MajorShareholder.QuantityAndShareholdingRatio(
                quantity=dart_atoi(resp.get("trmend_posesn_stock_co")),
                shareholding_ratio=dart_atoi(resp.get("trmend_posesn_stock_qota_rt")),
            ),
            remarks=resp.get("rm"),
        )


@dataclass(frozen=True)
class LargestShareholderChange(BusinessReportItemBase):
    changed_at: date  # change_on
    largest_shareholder_name: str  # mxmm_shrholdr_nm
    quantity: int  # posesn_stock_co
    shareholding_ratio: float  # qota_rt
    cause: str  # change_cause
    remarks: str  # rm

    @staticmethod
    def from_dart_resp(resp):
        return LargestShareholderChange(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            changed_at=datetime.strptime(resp.get("change_on"), "%Y년 %m월 %d일").date(),
            largest_shareholder_name=resp.get("mxmm_shrholdr_nm"),
            quantity=dart_atoi(resp.get("posesn_stock_co")),
            shareholding_ratio=dart_atoi(resp.get("qota_rt").replace("%", "")),
            cause=resp.get("change_cause"),
            remarks=resp.get("rm"),
        )


@dataclass(frozen=True)
class MinorityShareholdersStatus(BusinessReportItemBase):
    minority_shareholders_count: int  # shrholdr_co
    total_shareholders_count: Optional[int]  # shrholdr_tot_co
    minority_shareholders_ratio: float  # shrholdr_rate
    minority_shares: int  # hold_stock_co
    total_shares: Optional[int]  # stock_tot_co
    minority_shares_ratio: float  # hold_stock_rate

    @staticmethod
    def from_dart_resp(resp):
        return MinorityShareholdersStatus(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            minority_shareholders_count=dart_atoi(resp.get("shrholdr_co")),
            total_shareholders_count=(
                dart_atoi(resp.get("shrholdr_tot_co")) if resp.get("shrholdr_tot_co") != "-" else None
            ),
            minority_shares_ratio=dart_atoi(resp.get("shrholdr_rate").replace("%", "")),
            minority_shares=dart_atoi(resp.get("hold_stock_co")),
            total_shares=dart_atoi(resp.get("stock_tot_co")) if resp.get("stock_tot_co") != "-" else None,
            minority_shareholders_ratio=dart_atoi(resp.get("hold_stock_rate").replace("%", "")),
        )


@dataclass(frozen=True)
class Director(BusinessReportItemBase):
    name: str  # nm
    gender: str  # sexdstn
    birth_year_month: str  # birth_ym
    position: str  # ofcps
    is_registered: bool  # rgist_exctv_at
    is_full_time: bool  # fte_at
    work_in_charge: str  # chrg_job
    career_info: str  # main_career
    relation_to_major_shareholder: Optional[str]  # mxmm_shrholdr_relate
    tenure: str  # hffc_pd
    tenure_end_date: Optional[date]  # tenure_end_on

    @staticmethod
    def from_dart_resp(resp):
        return Director(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            name=resp.get("nm"),
            gender=resp.get("sexdstn"),
            birth_year_month=resp.get("birth_ym"),
            position=resp.get("ofcps"),
            is_registered=True if resp.get("rgist_exctv_at", "").startswith("등기") else False,
            is_full_time=True if resp.get("fte_at", "").startswith("상근") else False,
            work_in_charge=resp.get("chrg_job"),
            career_info=resp.get("main_career"),
            relation_to_major_shareholder=resp.get("mxmm_shrholdr_relate"),
            tenure=resp.get("hffc_pd"),
            tenure_end_date=(
                datetime.strptime(resp.get("tenure_end_on"), "%Y년 %m월 %d일").date()
                if resp.get("tenure_end_on") != "-"
                else None
            ),
        )


@dataclass(frozen=True)
class EmployeeStatus(BusinessReportItemBase):
    division: str  # fo_bbm
    gender: str  # sexdstn

    @dataclass(frozen=True)
    class LegacyEmploymentStatus:
        full_time: Optional[int]  # reform_bfe_emp_co_rgllbr
        contract: Optional[int]  # reform_bfe_emp_co_cnttk
        other: Optional[int]  # reform_bfe_emp_co_etc

    legacy_employment_status: LegacyEmploymentStatus

    @dataclass(frozen=True)
    class EmploymentStatus:
        total: int  # rgllbr_co, cnttk_co
        part_time: Optional[int]  # rgllbr_abacpt_labrr_co, cnttk_abacpt_labrr_co

    full_time: EmploymentStatus
    contract: EmploymentStatus
    total: int  # sm
    average_years_of_employment: float  # avrg_cnwk_sdytrn
    total_annual_salary: Optional[int]  # fyer_salary_totamt
    average_annual_salary: Optional[int]  # jan_salary_am
    remarks: str  # rm

    @staticmethod
    def from_dart_resp(resp):
        return EmployeeStatus(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            division=resp.get("fo_bbm"),
            gender=resp.get("sexdstn"),
            legacy_employment_status=EmployeeStatus.LegacyEmploymentStatus(
                full_time=dart_atoi(resp.get("reform_bfe_emp_co_rgllbr"))
                if resp.get("reform_bfe_emp_co_rgllbr") != "-"
                else None,
                contract=dart_atoi(resp.get("reform_bfe_emp_co_cnttk"))
                if resp.get("reform_bfe_emp_co_cnttk") != "-"
                else None,
                other=dart_atoi(resp.get("reform_bfe_emp_co_etc"))
                if resp.get("reform_bfe_emp_co_etc") != "-"
                else None,
            ),
            full_time=EmployeeStatus.EmploymentStatus(
                total=dart_atoi(resp.get("rgllbr_co")),
                part_time=(
                    dart_atoi(resp.get("rgllbr_abacpt_labrr_co")) if resp.get("rgllbr_abacpt_labrr_co") != "-" else None
                ),
            ),
            contract=EmployeeStatus.EmploymentStatus(
                total=dart_atoi(resp.get("cnttk_co")),
                part_time=(
                    dart_atoi(resp.get("cnttk_abacpt_labrr_co")) if resp.get("cnttk_abacpt_labrr_co") != "-" else None
                ),
            ),
            total=dart_atoi(resp.get("sm")),
            average_years_of_employment=dart_atoi(resp.get("avrg_cnwk_sdytrn")),
            total_annual_salary=(
                dart_atoi(resp.get("fyer_salary_totamt")) if resp.get("fyer_salary_totamt") != "-" else None
            ),
            average_annual_salary=dart_atoi(resp.get("jan_salary_am")) if resp.get("jan_salary_am") != "-" else None,
            remarks=resp.get("rm"),
        )


@dataclass(frozen=True)
class IndividualExecutiveStatus(BusinessReportItemBase):
    name: str  # nm
    position: str  # ofcps
    total: int  # mendng_totamt
    compensation_not_included_in_total: Optional[int]  # mendng_totamt_ct_incls_mendng

    @staticmethod
    def from_dart_resp(resp):
        return IndividualExecutiveStatus(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            name=resp.get("nm"),
            position=resp.get("ofcps"),
            total=dart_atoi(resp.get("mendng_totamt")),
            compensation_not_included_in_total=dart_atoi(resp.get("mendng_totamt_ct_incls_mendng"))
            if resp.get("mendng_totamt_ct_incls_mendng") not in ("-", "\u3000-")
            else None,
        )


@dataclass(frozen=True)
class ExecutiveCompensationStatus(BusinessReportItemBase):
    headcount: int  # nmpr
    total: int  # mendng_totamt
    average: int  # jan_avrg_mendng_am
    remarks: str  # rm

    @staticmethod
    def from_dart_resp(resp):
        return ExecutiveCompensationStatus(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            headcount=dart_atoi(resp.get("nmpr")),
            total=dart_atoi(resp.get("mendng_totamt")),
            average=dart_atoi(resp.get("jan_avrg_mendng_am")),
            remarks=resp.get("rm"),
        )


class BusinessReports:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_capital_variation(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[CapitalVariation]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("irdsSttus", **params)

        if not resp.get("list"):
            return tuple()
        if len(resp.get("list")) == 1 and resp["list"][0].get("isu_dcrs_qy") == "-":
            return tuple()

        return tuple(CapitalVariation.from_dart_resp(i) for i in resp.get("list", []))

    def get_dividend_info(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[DividendInfo]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("alotMatter", **params)

        return tuple(DividendInfo.from_dart_resp(i) for i in resp.get("list", []) if i.get("thstrm") != "-")

    def get_treasury_shares_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[TreasurySharesStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("tesstkAcqsDspsSttus", **params)

        return tuple(TreasurySharesStatus.from_dart_resp(i) for i in resp.get("list", []) if i.get("trmend_qy") != "-")

    def get_major_shareholders_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[MajorShareholder]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("hyslrSttus", **params)

        return tuple(
            MajorShareholder.from_dart_resp(i) for i in resp.get("list", []) if i.get("trmend_posesn_stock_co") != "-"
        )

    def get_largest_shareholder_changes(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[LargestShareholderChange]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("hyslrChgSttus", **params)

        return tuple(
            LargestShareholderChange.from_dart_resp(i) for i in resp.get("list", []) if i.get("change_on") != "-"
        )

    def get_minority_shareholders_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[MinorityShareholdersStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("mrhlSttus", **params)

        return tuple(MinorityShareholdersStatus.from_dart_resp(i) for i in resp.get("list", []))

    def get_directors(self, corporation_code: str, business_year: int, report_code: ReportCode) -> Tuple[Director]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("exctvSttus", **params)

        return tuple(Director.from_dart_resp(i) for i in resp.get("list", []))

    def get_employee_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[EmployeeStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("empSttus", **params)

        return tuple(EmployeeStatus.from_dart_resp(i) for i in resp.get("list", []))

    def get_individual_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[IndividualExecutiveStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("hmvAuditIndvdlBySttus", **params)

        return tuple(IndividualExecutiveStatus.from_dart_resp(i) for i in resp.get("list", []))

    def get_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[ExecutiveCompensationStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("hmvAuditAllSttus", **params)

        return tuple(ExecutiveCompensationStatus.from_dart_resp(i) for i in resp.get("list", []))

    def get_top_5_individual_executive_compensation(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[IndividualExecutiveStatus]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("indvdlByPay", **params)

        return tuple(IndividualExecutiveStatus.from_dart_resp(i) for i in resp.get("list", []))

    def get_investment_in_other_corporations(self):
        pass
