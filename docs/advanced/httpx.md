# HTTPX 클라이언트 사용하기

!!! warning "Be careful of using"
    HTTPX is currently in beta. for further information, please visit [HTTPX](https://www.python-httpx.org/)

## Install httpx

To use httpx client, extra requirements should be installed

```bash
pip install pyopendart[httpx]
```

## Using httpx client

You can use httpx client instead of requests client by passing parameter to client constructor.

```python
from pyopendart.clients.http import HttpxOpenApiClient

client = DataframeDisclosureClient(
    "YOUR API KEY", client_cls=HttpxOpenApiClient
)

# or
httpx_client = HttpxClient("")
client = DataframeDisclosureClient("YOUR API KEY", client=httpx)

```