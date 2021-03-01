# API 설정

## 네트워크 옵션 설정하기

네트워크 상황에 맞추어 각 클라이언트에 타임아웃을 설정할 수 있습니다.

### Available Options

| Name                     | Type                        |
| ------------------------ | --------------------------- |
| default_timeout          | Requests type or Httpx type |
| default_download_timeout | Requests type or Httpx type |
| use_connection_pool      | `bool`                      |


```python
from pyopendart.api.dataframe import FillingApi
from pyopendart.api.http.requests import RequestsOpenApiClient

client = RequestsOpenApiClient("YOUR API KEY", default_timeout=15)
api = FillingApi(client=client)

df = api.get_company_overview("00126380")
```

!!! note
    기본적으로는 requests 형식의 타임아웃을 사용하지만 HTTPX 클라이언트를 사용한다면 HTTPX 형식의 타임아웃도 설정할 수 있습니다.

## 필드명 변환 옵션 설정하기

각 api 들은 dart의 축약된 필드명을 자세한 한글, 영어 필드명으로 변환하는 옵션을 가지고 있습니다. 이 옵션을 조작하여 기본으로 영어 필드명으로 변환되는 것을 한글로 변환되게 하거나 또는 필드명 수정을 사용하지 않게 할 수 있습니다.

```python
def some_api(
    ...
    *,
    rename: Optional[RenameMode] = RenameMode.ENG
)
```

## HTTPX 클라이언트 사용하기

!!! warning "Be careful of use"
    HTTPX is currently in beta. for further information, please visit [HTTPX](https://www.python-httpx.org/)

### Install httpx

To use httpx client, extra requirements should be installed

```bash
pip install pyopendart[httpx]
```

### Using httpx client

You can use httpx client instead of requests client by passing parameter to client constructor.

```python
from pyopendart.api.http.httpx import HttpxOpenApiClient

httpx_client = HttpxOpenApiClient("YOUR API KEY", default_timeout=7, default_download_timeout=17, use_connection_pool=True)
client = DataframeDisclosureClient(client=httpx_client)
```

## 다른 클라이언트 사용하기

기본으로 제공되는 Requests, HTTPX 클라이언트는 OpenApiClient 인터페이스의 구현체입니다. 해당 인터페이스를 구현하여 자신만의 클라이언트를 이용할 수 있습니다

```python
from pyopendart.api.dataframe import FillingApi
from pyopendart.api.http import DartApiParamType, OpenApiClient

class MyOwnOpenApiClient(OpenApiClient):
    ...

api = FillingApi(client=MyOwnClient("YOUR API KEY"))
```