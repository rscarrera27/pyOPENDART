# 상장기업 재무정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.clients import DataframeFinancialInformationClient
    from pyopendart.enums import ReportType
    ```

=== "Namedtuple"
    
    ```python
    from pyopendart.clients import NamedtupleFinancialInformationClient
    from pyopendart.enums import ReportType
    ```

=== "Dict"
    
    ```python
    from pyopendart.clients import FinancialInformationClient
    from pyopendart.enums import ReportType
    ```

## 단일ㆍ다중회사 주요계정
### Parameter

| Name              | Type         | DART Name  |
| ----------------- | ------------ | ---------- |
| corporation_codes | `List[str]`  | corp_code  |
| business_year     | `int`        | bsns_year  |
| report_type       | `ReportType` | reprt_code |

### Usage

=== "Dataframe"

    ```python
    client = DataframeFinancialInformationClient("YOUR API KEY")

    df, meta = get_financial_statements_of_major_accounts(
        corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1
    )
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleFinancialInformationClient("YOUR API KEY")

    financial_statements_of_major_accounts = get_financial_statements_of_major_accounts(
        corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1
    )
    ```

=== "Dict"
    
    ```python
    client = FinancialInformationClient("YOUR API KEY")

    financial_statements_of_major_accounts = get_financial_statements_of_major_accounts(
        corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1
    )
    ```

## 단일회사 전체 재무제표
### Parameter

| Name                         | Type                         | DART Name  |
| ---------------------------- | ---------------------------- | ---------- |
| corporation_codes            | `List[str]`                  | corp_code  |
| business_year                | `int`                        | bsns_year  |
| report_type                  | `ReportType`                 | reprt_code |
| financial_statement_division | `FinancialStatementDivision` | fs_div     |

### Usage

=== "Dataframe"

    ```python
    client = DataframeFinancialInformationClient("YOUR API KEY")

    df, m = client.get_full_financial_statements(
        corporation_code="00293886", business_year=2019, report_type=ReportType.Q1\
    )
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleFinancialInformationClient("YOUR API KEY")

    full_financial_statements = client.get_full_financial_statements(
        corporation_code="00293886", business_year=2019, report_type=ReportType.Q1\
    )
    ```

=== "Dict"
    
    ```python
    client = FinancialInformationClient("YOUR API KEY")

    full_financial_statements = client.get_full_financial_statements(
        corporation_code="00293886", business_year=2019, report_type=ReportType.Q1\
    )
    ```

## XBRL택소노미 재무제표양식
### Parameter

| Name                              | Type  | DART Name |
| --------------------------------- | ----- | --------- |
| detailed_financial_statement_type | `str` | sj_div    |

### Usage

=== "Dataframe"

    ```python
    client = DataframeFinancialInformationClient("YOUR API KEY")
    
    df, _ = client.get_xbrl_taxonomies("BS1")
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleFinancialInformationClient("YOUR API KEY")

    xbrl_taxonomies = client.get_xbrl_taxonomies("BS1")
    ```

=== "Dict"
    
    ```python
    client = FinancialInformationClient("YOUR API KEY")

    xbrl_taxonomies = client.get_xbrl_taxonomies("BS1")
    ```
