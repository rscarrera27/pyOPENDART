from collections import namedtuple
from typing import Sequence

from pyopendart.clients.dict.business_report import BusinessReportClient
from pyopendart.enums import ReportType

ChangeInEquity = namedtuple(
    "ChangeInEquity",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'isu_dcrs_de',
        'isu_dcrs_stle',
        'isu_dcrs_stock_knd',
        'isu_dcrs_qy',
        'isu_dcrs_mstvdv_fval_amount',
        'isu_dcrs_mstvdv_amount',
    ],
)

DividendInfo = namedtuple(
    "DividendInfo",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'se',
        'stock_knd',
        'thstrm',
        'frmtrm',
        'lwfr',
    ],
    defaults=[""] * 9,
)

TreasurySharesStatus = namedtuple(
    "TreasurySharesStatus",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'acqs_mth1',
        'acqs_mth2',
        'acqs_mth3',
        'stock_knd',
        'bsis_qy',
        'change_qy_acqs',
        'change_qy_dsps',
        'change_qy_incnr',
        'trmend_qy',
        'rm',
    ],
)


MajorShareholder = namedtuple(
    "MajorShareholder",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'stock_knd',
        'nm',
        'relate',
        'bsis_posesn_stock_co',
        'bsis_posesn_stock_qota_rt',
        'trmend_posesn_stock_co',
        'trmend_posesn_stock_qota_rt',
        'rm',
    ],
    defaults=[""] * 12,
)


ChangesInMajorShareholder = namedtuple(
    "ChangesInMajorShareholder",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'change_on',
        'mxmm_shrholdr_nm',
        'posesn_stock_co',
        'qota_rt',
        'change_cause',
        'rm',
    ],
)

MinorityShareholdersStatus = namedtuple(
    "MinorityShareholdersStatus",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'se',
        'shrholdr_co',
        'shrholdr_tot_co',
        'shrholdr_rate',
        'hold_stock_co',
        'stock_tot_co',
        'hold_stock_rate',
    ],
)

Executive = namedtuple(
    "Executive",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'nm',
        'sexdstn',
        'birth_ym',
        'ofcps',
        'rgist_exctv_at',
        'fte_at',
        'chrg_job',
        'main_career',
        'mxmm_shrholdr_relate',
        'hffc_pd',
        'tenure_end_on',
    ],
)

EmploymentStatus = namedtuple(
    "EmploymentStatus",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        'fo_bbm',
        'sexdstn',
        'reform_bfe_emp_co_rgllbr',
        'reform_bfe_emp_co_cnttk',
        'reform_bfe_emp_co_etc',
        'rgllbr_co',
        'rgllbr_abacpt_labrr_co',
        'cnttk_co',
        'cnttk_abacpt_labrr_co',
        'sm',
        'avrg_cnwk_sdytrn',
        'fyer_salary_totamt',
        'jan_salary_am',
        'rm',
    ],
)

IndividualExecutiveCompensationStatus = namedtuple(
    "IndividualExecutiveCompensationStatus",
    ['rcept_no', 'corp_cls', 'corp_code', 'corp_name', 'nm', 'ofcps', 'mendng_totamt', 'mendng_totamt_ct_incls_mendng'],
)

ExecutiveCompensationStatus = namedtuple(
    "ExecutiveCompensationStatus",
    ['rcept_no', 'corp_cls', 'corp_code', 'corp_name', "nmpr", "mendng_totamt", "jan_avrg_mendng_am", "rm"],
)

InvestmentInOtherCorporation = namedtuple(
    "InvestmentInOtherCorporation",
    [
        'rcept_no',
        'corp_cls',
        'corp_code',
        'corp_name',
        "inv_prm",
        "frst_acqs_de",
        "invstmnt_purps",
        "frst_acqs_amount",
        "bsis_blce_qy",
        "bsis_blce_qota_rt",
        "bsis_blce_acntbk_amount",
        "incrs_dcrs_acqs_dsps_qy",
        "incrs_dcrs_acqs_dsps_amount",
        "incrs_dcrs_evl_lstmn",
        "trmend_blce_qy",
        "trmend_blce_qota_rt",
        "trmend_blce_acntbk_amount",
        "recent_bsns_year_fnnr_sttus_tot_assets",
        "recent_bsns_year_fnnr_sttus_thstrm_ntpf",
    ],
)


class NamedtupleBusinessReportClient(BusinessReportClient):
    def get_changes_in_equity(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[ChangeInEquity]:
        items = super(NamedtupleBusinessReportClient, self).get_changes_in_equity(
            corporation_code, business_year, report_type
        )
        return [ChangeInEquity(**i) for i in items]

    def get_dividend_info(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[DividendInfo]:
        items = super(NamedtupleBusinessReportClient, self).get_dividend_info(
            corporation_code, business_year, report_type
        )
        return [DividendInfo(**i) for i in items]

    def get_treasury_shares_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[TreasurySharesStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_treasury_shares_status(
            corporation_code, business_year, report_type
        )
        return [TreasurySharesStatus(**i) for i in items]

    def get_major_shareholders(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[MajorShareholder]:
        items = super(NamedtupleBusinessReportClient, self).get_major_shareholders(
            corporation_code, business_year, report_type
        )
        return [MajorShareholder(**i) for i in items]

    def get_changes_in_major_shareholder(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[ChangesInMajorShareholder]:
        items = super(NamedtupleBusinessReportClient, self).get_changes_in_major_shareholder(
            corporation_code, business_year, report_type
        )
        return [ChangesInMajorShareholder(**i) for i in items]

    def get_minority_shareholders_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[MinorityShareholdersStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_minority_shareholders_status(
            corporation_code, business_year, report_type
        )
        return [MinorityShareholdersStatus(**i) for i in items]

    def get_executives(self, corporation_code: str, business_year: int, report_type: ReportType) -> Sequence[Executive]:
        items = super(NamedtupleBusinessReportClient, self).get_executives(corporation_code, business_year, report_type)
        return [Executive(**i) for i in items]

    def get_employment_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[EmploymentStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_employment_status(
            corporation_code, business_year, report_type
        )
        return [EmploymentStatus(**i) for i in items]

    def get_individual_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[IndividualExecutiveCompensationStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_individual_executive_compensation_status(
            corporation_code, business_year, report_type
        )
        return [IndividualExecutiveCompensationStatus(**i) for i in items]

    def get_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[ExecutiveCompensationStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_executive_compensation_status(
            corporation_code, business_year, report_type
        )
        return [ExecutiveCompensationStatus(**i) for i in items]

    def get_top_5_individual_executive_compensation(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[IndividualExecutiveCompensationStatus]:
        items = super(NamedtupleBusinessReportClient, self).get_top_5_individual_executive_compensation(
            corporation_code, business_year, report_type
        )
        return [IndividualExecutiveCompensationStatus(**i) for i in items]

    def get_investment_in_other_corporations(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[InvestmentInOtherCorporation]:
        items = super(NamedtupleBusinessReportClient, self).get_investment_in_other_corporations(
            corporation_code, business_year, report_type
        )
        return [InvestmentInOtherCorporation(**i) for i in items]
