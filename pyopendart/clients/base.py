from typing import Any, Type

from pyopendart.clients.http import OpenApiClient, RequestsOpenApiClient


class ClientBase:
    def __init__(
        self,
        api_key: str,
        client: OpenApiClient = None,
        client_cls: Type[OpenApiClient] = RequestsOpenApiClient,
        default_timeout: Any = None,
        default_download_timeout: Any = None,
        **kwargs,
    ) -> None:
        if client:
            self.client = client
            self.client.api_key = api_key
        else:
            self.client = client_cls(api_key, default_timeout, default_download_timeout, **kwargs)
