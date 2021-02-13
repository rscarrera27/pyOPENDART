# 타임아웃 설정하기

네트워크 상황에 맞추어 각 클라이언트에 타임아웃을 설정할 수 있습니다.

```python
from pyopendart.clients import DisclosureClient

company_overview = (
    DisclosureClient("YOUR API KEY", default_timeout=7)
    .get_company_overview("00126380")
)
```

## HTTPX 클라이언트

기본적으로는 requests 형식의 타임아웃을 사용하지만 HTTPX 클라이언트를 사용한다면 HTTPX 형식의 타임아웃을 설정할 수 있습니다.