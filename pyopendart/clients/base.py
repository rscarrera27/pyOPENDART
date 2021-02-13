from typing import Any, Type

from pyopendart.clients.http import DartClient, RequestsDartClient


class ClientBase:
    def __init__(
        self,
        api_key: str,
        client: DartClient = None,
        client_cls: Type[DartClient] = RequestsDartClient,
        default_timeout: Any = None,
        default_download_timeout: Any = None,
        **kwargs,
    ) -> None:
        if client:
            self.client = client
        else:
            self.client = client_cls(api_key, default_timeout, default_download_timeout, **kwargs)
