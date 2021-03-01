from typing import Optional

from pyopendart.api.http import OpenApiClient
from pyopendart.api.http.requests import RequestsOpenApiClient


class ApiBase:
    def __init__(self, api_key: str = None, *, client: Optional[OpenApiClient] = None):
        if client:
            self.client = client
        else:
            self.client = RequestsOpenApiClient(api_key)
