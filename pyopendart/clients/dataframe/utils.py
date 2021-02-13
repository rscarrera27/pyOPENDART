from datetime import datetime
from typing import Any, Callable, Dict, Optional, Sequence, Tuple

import pandas as pd
from dateutil.parser import parse as datetime_parse

from pyopendart.enums import FinancialStatementDivision, FinancialStatementType, Market, ReportType
from pyopendart.utils import dart_atoi, is_dart_null

DEFAULT_RENAME_MAPPING = {
    "corp_code": "corporation_code",
    "corp_name": "corporation_name",
    "corp_name_eng": "corporation_name_en",
    "stock_code": "stock_code",
    "corp_cls": "market",
    "report_nm": "report_name",
    "rcept_no": "receipt_no",
    "flr_nm": "filler",
    "rcept_dt": "receipt_date",
    "rm": "remarks",
    "ceo_nm": "representative",
    "jurir_no": "corporation_registration_number",
    "bizr_no": "taxpayer_registration_number",
    "adres": "address",
    "hm_url": "homepage_url",
    "ir_url": "ir_url",
    "phn_no": "phone_number",
    "fax_no": "fax_number",
    "induty_code": "industry_code",
    "est_dt": "establishment_date",
    "acc_mt": "ending_month_of_fiscal_year",
    "isu_dcrs_de": "date",
    "isu_dcrs_stle": "title",
    "isu_dcrs_stock_knd": "stock_type",
    "isu_dcrs_qy": "quantity",
    "isu_dcrs_mstvdv_fval_amount": "face_value",
    "isu_dcrs_mstvdv_amount": "issue_price",
    "se": "title",
    "stock_knd": "stock_type",
    "thstrm": "current_term",
    "frmtrm": "prev_term",
    "lwfr": "prev_prev_term",
    "acqs_mth1": "acquisition_method_l",
    "acqs_mth2": "acquisition_method_m",
    "acqs_mth3": "acquisition_method_s",
    "bsis_qy": "quantity_term_start",
    "change_qy_acqs": "acquired",
    "change_qy_dsps": "disposed",
    "change_qy_incnr": "retired",
    "trmend_qy": "quantity_term_end",
    "nm": "name",
    "relate": "relation",
    "bsis_posesn_stock_co": "term_start_quantity",
    "bsis_posesn_stock_qota_rt": "term_start_shareholding_ratio",
    "trmend_posesn_stock_co": "term_end_quantity",
    "trmend_posesn_stock_qota_rt": "term_end_shareholding_ratio",
    "change_on": "changed_at",
    "mxmm_shrholdr_nm": "shareholder_name",
    "posesn_stock_co": "quantity",
    "qota_rt": "ratio",
    "change_cause": "reason",
    "shrholdr_co": "minority_shareholders",
    "shrholdr_tot_co": "total_shareholders",
    "shrholdr_rate": "minority_shareholders_ratio",
    "hold_stock_co": "minority_shares",
    "stock_tot_co": "total_shares",
    "hold_stock_rate": "minority_shares_ratio",
    "sexdstn": "gender",
    "birth_ym": "birth_year_month",
    "ofcps": "position",
    "rgist_exctv_at": "is_registered",
    "fte_at": "is_full_time",
    "chrg_job": "charge",
    "main_career": "career_info",
    "mxmm_shrholdr_relate": "relation",
    "hffc_pd": "tenure",
    "tenure_end_on": "tenure_end_date",
    "fo_bbm": "division",
    "reform_bfe_emp_co_rgllbr": "legacy_regular_employees",
    "reform_bfe_emp_co_cnttk": "legacy_contract_employees",
    "reform_bfe_emp_co_etc": "legacy_other_employees",
    "rgllbr_co": "regular_employees",
    "rgllbr_abacpt_labrr_co": "part_time_regular_employees",
    "cnttk_co": "contract_employees",
    "cnttk_abacpt_labrr_co": "part_time_contract_employees",
    "sm": "total_employees_count",
    "avrg_cnwk_sdytrn": "average_years_of_employment",
    "fyer_salary_totamt": "total_annual_salary",
    "jan_salary_am": "average_annual_salary",
    "mendng_totamt": "total",
    "mendng_totamt_ct_incls_mendng": "compensation_not_included_in_total",
    "nmpr": "headcount",
    "jan_avrg_mendng_am": "average",
    "inv_prm": "invested_corporation_name",
    "frst_acqs_de": "first_acquisition_date",
    "invstmnt_purps": "purpose",
    "frst_acqs_amount": "first_acquired_amount",
    "bsis_blce_qy": "term_start_quantity",
    "bsis_blce_qota_rt": "term_start_shares_ratio",
    "bsis_blce_acntbk_amount": "term_start_book_value",
    "incrs_dcrs_acqs_dsps_qy": "acquired_or_disposed_quantity",
    "incrs_dcrs_acqs_dsps_amount": "acquired_or_disposed_amount",
    "incrs_dcrs_evl_lstmn": "gain_or_loss",
    "trmend_blce_qy": "term_end_quantity",
    "trmend_blce_qota_rt": "term_end_shares_ratio",
    "trmend_blce_acntbk_amount": "term_end_book_value",
    "recent_bsns_year_fnnr_sttus_tot_assets": "last_recent_fiscal_year_asset_total",
    "recent_bsns_year_fnnr_sttus_thstrm_ntpf": "last_recent_fiscal_year_net_income",
    'reprt_code': "report_type",
    'bsns_year': "business_year",
    'fs_div': "division",
    'fs_nm': "division_name",
    'sj_div': "type",
    'sj_nm': "type_name",
    'account_nm': "account_name",
    'thstrm_nm': "current_term_name",
    'thstrm_dt': "current_term_date",
    'thstrm_amount': "current_term_amount",
    'thstrm_add_amount': "current_term_cumulative_amount",
    'frmtrm_nm': "prev_term_name",
    'frmtrm_dt': "prev_term_date",
    'frmtrm_amount': "prev_term_amount",
    'frmtrm_add_amount': "prev_term_cumulative_amount",
    'bfefrmtrm_nm': "prev_prev_term_name",
    'bfefrmtrm_dt': "prev_prev_term_date",
    'bfefrmtrm_amount': "prev_prev_term_amount",
    'ord': "account_order",
    'account_id': "account_id",
    'account_detail': "statement_of_changes_in_equity_column",
    'frmtrm_q_nm': "prev_quarter_name",
    'frmtrm_q_amount': "prev_quarter_amount",
    'bsns_de': "applied_date",
    'label_kor': "label_ko",
    'label_eng': "label_en",
    'data_tp': "data_type",
    'ifrs_ref': "ifrs_ref",
    "report_tp": "major_shareholder_report_type",
    "repror": "reporter",
    "stkqy": "shares_quantity",
    "stkqy_irds": "increased_or_decreased_quantity",
    "stkrt": "shares_ratio",
    "stkrt_irds": "increased_or_decreased_ratio",
    "ctr_stkqy": "contract_shares_quantity",
    "ctr_stkrt": "contract_shares_ratio",
    "report_resn": "reason",
    "isu_exctv_rgist_at": "is_registered",
    "isu_exctv_ofcps": "position",
    "isu_main_shrholdr": "shareholder_detail",
    "sp_stock_lmp_cnt": "shares_quantity",
    "sp_stock_lmp_irds_cnt": "increased_or_decreased_quantity",
    "sp_stock_lmp_rate": "shares_ratio",
    "sp_stock_lmp_irds_rate": "increased_or_decreased_ratio",
}

DEFAULT_CONVERTERS = {
    "corp_cls": Market,
    "rcept_dt": lambda v: datetime_parse(v).date(),
    "jurir_no": dart_atoi,
    "bizr_no": dart_atoi,
    "induty_code": dart_atoi,
    "est_dt": lambda v: datetime_parse(v).date(),
    "acc_mt": dart_atoi,
    "isu_dcrs_de": lambda v: datetime_parse(v).date() if not is_dart_null(v) else v,
    "isu_dcrs_qy": dart_atoi,
    "isu_dcrs_mstvdv_fval_amount": dart_atoi,
    "isu_dcrs_mstvdv_amount": dart_atoi,
    "thstrm": dart_atoi,
    "frmtrm": dart_atoi,
    "lwfr": dart_atoi,
    "bsis_qy": dart_atoi,
    "change_qy_acqs": dart_atoi,
    "change_qy_dsps": dart_atoi,
    "change_qy_incnr": dart_atoi,
    "trmend_qy": dart_atoi,
    "bsis_posesn_stock_co": dart_atoi,
    "bsis_posesn_stock_qota_rt": dart_atoi,
    "trmend_posesn_stock_co": dart_atoi,
    "trmend_posesn_stock_qota_rt": dart_atoi,
    "posesn_stock_co": dart_atoi,
    "qota_rt": lambda v: dart_atoi(v.replace("%", "")),
    "change_on": lambda v: datetime.strptime(v, "%Y년 %m월 %d일").date() if not is_dart_null(v) else "",
    "shrholdr_co": dart_atoi,
    "shrholdr_tot_co": dart_atoi,
    "shrholdr_rate": lambda v: dart_atoi(v.replace("%", "")),
    "hold_stock_co": dart_atoi,
    "stock_tot_co": dart_atoi,
    "hold_stock_rate": lambda v: dart_atoi(v.replace("%", "")),
    "rgist_exctv_at": lambda v: True if v.startswith("등기") else False,
    "fte_at": lambda v: True if v.startswith("상근") else False,
    "tenure_end_on": lambda v: datetime.strptime(v, "%Y년 %m월 %d일").date() if not is_dart_null(v) else "",
    "reform_bfe_emp_co_rgllbr": dart_atoi,
    "reform_bfe_emp_co_cnttk": dart_atoi,
    "reform_bfe_emp_co_etc": dart_atoi,
    "rgllbr_co": dart_atoi,
    "rgllbr_abacpt_labrr_co": dart_atoi,
    "cnttk_co": dart_atoi,
    "cnttk_abacpt_labrr_co": dart_atoi,
    "sm": dart_atoi,
    "fyer_salary_totamt": dart_atoi,
    "jan_salary_am": dart_atoi,
    "mendng_totamt": dart_atoi,
    "mendng_totamt_ct_incls_mendng": dart_atoi,
    "nmpr": dart_atoi,
    "jan_avrg_mendng_am": dart_atoi,
    "frst_acqs_de": lambda v: datetime_parse(v) if not is_dart_null(v) else "",
    "frst_acqs_amount": dart_atoi,
    "bsis_blce_qy": dart_atoi,
    "bsis_blce_qota_rt": dart_atoi,
    "bsis_blce_acntbk_amount": dart_atoi,
    "incrs_dcrs_acqs_dsps_qy": dart_atoi,
    "incrs_dcrs_acqs_dsps_amount": dart_atoi,
    "incrs_dcrs_evl_lstmn": dart_atoi,
    "trmend_blce_qy": dart_atoi,
    "trmend_blce_qota_rt": dart_atoi,
    "trmend_blce_acntbk_amount": dart_atoi,
    "recent_bsns_year_fnnr_sttus_tot_assets": dart_atoi,
    "recent_bsns_year_fnnr_sttus_thstrm_ntpf": dart_atoi,
    "reprt_code": lambda v: ReportType(dart_atoi(v)),
    "bsns_year": dart_atoi,
    "fs_div": FinancialStatementDivision,
    "sj_div": FinancialStatementType,
    "thstrm_amount": dart_atoi,
    "thstrm_add_amount": dart_atoi,
    "frmtrm_amount": dart_atoi,
    "frmtrm_add_amount": dart_atoi,
    "bfefrmtrm_amount": dart_atoi,
    "ord": dart_atoi,
    "frmtrm_q_amount": dart_atoi,
    "bsns_de": lambda v: datetime.strptime(v, "%Y%m%d").date(),
    "stkqy": dart_atoi,
    "stkqy_irds": dart_atoi,
    "stkrt": dart_atoi,
    "stkrt_irds": dart_atoi,
    "ctr_stkqy": dart_atoi,
    "ctr_stkrt": dart_atoi,
    "isu_exctv_rgist_at": lambda v: True if v.startswith("등기") else False,
    "sp_stock_lmp_cnt": dart_atoi,
    "sp_stock_lmp_irds_cnt": dart_atoi,
    "sp_stock_lmp_rate": dart_atoi,
    "sp_stock_lmp_irds_rate": dart_atoi,
}


def get_converters(*keys) -> Dict[str, Callable[[str], Any]]:
    converters = {}
    for k in keys:
        converters[k] = DEFAULT_CONVERTERS[k]

    return converters


def construct_dataframe(
    items: Sequence[Any],
    converters: Dict[str, Callable[[str], Any]] = None,
    sort_by: list = None,
    sort_asc: bool = True,
    rename: Optional[dict] = None,
    metadata_cols: Optional[list] = None,
    index: Optional[list] = None,
) -> Tuple[pd.DataFrame, Optional[dict]]:
    df = pd.DataFrame(items)

    if converters:
        for k, f in converters.items():
            df[k] = df[k].apply(f)

    if sort_by:
        df = df.sort_values(sort_by, ascending=sort_asc)

    if rename:
        columns = {k: rename.get(k, k) for k in df.columns.values}
        df = df.rename(
            columns=columns,
        )

    metadata = None
    if metadata_cols:
        metadata = {k: df[k][0] for k in metadata_cols}
        df = df.drop(columns=metadata_cols)

    if index:
        df = df.set_index(index)

    return df, metadata
