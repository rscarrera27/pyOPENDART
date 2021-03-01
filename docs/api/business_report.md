# 사업보고서 주요정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.api.dataframe import BusinessReportApi
    from pyopendart.enums import ReportType
    ```

=== "Dict"
    
    ```python
    from pyopendart.api.dict import BusinessReportApi
    from pyopendart.enums import ReportType
    ```


## Parameter

| Name             | Type         | DART Name  |
| ---------------- | ------------ | ---------- |
| corporation_code | `str`        | corp_code  |
| business_year    | `int`        | bsns_year  |
| report_type      | `ReportType` | reprt_code |

## 증ㆍ감자 현황 (자본금 변동사항)


=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_changes_in_equity(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    changes_in_equity = api.get_changes_in_equity(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 배당에 관한 사항

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_dividend_info(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    dividend_info = api.get_dividend_info(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 자기주식 취득 및 처분 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_treasury_shares_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    treasury_shares_status = api.get_treasury_shares_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 최대주주 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_major_shareholders(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    major_shareholders = api.get_major_shareholders(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 최대주주 변동 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_changes_in_major_shareholder(
        corporation_code="00356361", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    changes_in_major_shareholder = api.get_changes_in_major_shareholder(
        corporation_code="00356361", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 소액주주 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_minority_shareholders_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    minority_shareholders_status = api.get_minority_shareholders_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 임원 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_executives(
        corporation_code="00126380", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    executives = api.get_executives(
        corporation_code="00126380", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 직원 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_employment_status(
        corporation_code="00126380", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    employment_status = api.get_employment_status(
        corporation_code="00126380", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 이사ㆍ감사의 개인별 보수 현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_individual_executive_compensation_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    individual_executive_compensation_status = api.get_individual_executive_compensation_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 이사ㆍ감사 전체의 보수현황	

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_executive_compensation_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    executive_compensation_status = api.get_executive_compensation_status(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

## 개인별 보수지급 금액(5억이상 상위5인)

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_top_5_individual_executive_compensation(
        corporation_code="00126380", business_year=2019, report_type=ReportType.Q1
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    top_5_individual_executive_compensation = api.get_top_5_individual_executive_compensation(
        corporation_code="00126380", business_year=2019, report_type=ReportType.Q1
    )
    ```

## 타법인 출자현황

=== "Dataframe"

    ```python
    api = BusinessReportApi("YOUR API KEY")

    df = api.get_investment_in_other_corporations(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```

=== "Dict"
    
    ```python
    api = BusinessReportApi("YOUR API KEY")

    investment_in_other_corporations = api.get_investment_in_other_corporations(
        corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL
    )
    ```
