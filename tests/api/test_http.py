import os
from tempfile import TemporaryDirectory
from xml.etree.ElementTree import ElementTree

import pytest

from pyopendart.api.http.httpx import HttpxOpenApiClient
from pyopendart.api.http.requests import RequestsOpenApiClient
from pyopendart.exceptions import DartException
from tests.config import TEST_CLIENT_KEY

CLIENT_CLS = [RequestsOpenApiClient, HttpxOpenApiClient]
CLIENT_PARAMS = [
    dict(api_key=TEST_CLIENT_KEY),
    dict(api_key=TEST_CLIENT_KEY, default_timeout=3),
    dict(api_key=TEST_CLIENT_KEY, default_timeout=3, use_connection_pool=True),
]

RESOURCE_TEST_DATASET = [
    ("company", {"corp_code": "00126380"}),
    ("fnlttSinglAcnt", {"corp_code": "00126380", "bsns_year": "2019", "reprt_code": "11011"}),
]
RESOURCE_ERROR_TEST_DATASET = [
    ("company", {"crtfc_key": "notaapikey", "corp_code": "00126380"}),
    ("fnlttSinglAcnt", {"corp_code": "00126380", "bsns_year": "3000", "reprt_code": "11011"}),
]


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
@pytest.mark.parametrize("resource, params", RESOURCE_TEST_DATASET)
def test_json_resource(client_cls, client_params, resource, params):
    client = client_cls(**client_params)
    resp = client.json_resource(resource, params, timeout=3)

    assert isinstance(resp, dict)
    assert resp.get("status") is None
    assert resp.get("message") is None


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
@pytest.mark.parametrize("resource, params", RESOURCE_ERROR_TEST_DATASET)
def test_json_resource_error(client_cls, client_params, resource, params):
    client = client_cls(**client_params)

    with pytest.raises(DartException):
        client.json_resource(resource, params, timeout=3)


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
@pytest.mark.parametrize("resource, params", RESOURCE_TEST_DATASET)
def test_xml_resource(client_cls, client_params, resource, params):
    client = client_cls(**client_params)
    resp = client.xml_resource(resource, params, timeout=3)

    assert isinstance(resp, ElementTree)
    assert resp.find("status") is None
    assert resp.find("message") is None


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
@pytest.mark.parametrize("resource, params", RESOURCE_ERROR_TEST_DATASET)
def test_xml_resource_error(client_cls, client_params, resource, params):
    client = client_cls(**client_params)

    with pytest.raises(DartException):
        client.xml_resource(resource, params, timeout=3)


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
def test_zip_resource(client_cls, client_params):
    client = client_cls(**client_params)

    with TemporaryDirectory() as tempdir:
        client.zip_resource("document", {"rcept_no": "20190401004781"}, extract_to=tempdir)

        assert os.listdir(tempdir)


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
def test_zip_resource_error(client_cls, client_params):
    client = client_cls(**client_params)

    with pytest.raises(DartException):
        with TemporaryDirectory() as tempdir:
            client.zip_resource("document", {"rcept_no": "notrecieptno"}, extract_to=tempdir)


@pytest.mark.parametrize("client_cls", CLIENT_CLS)
@pytest.mark.parametrize("client_params", CLIENT_PARAMS)
def test_iter_list_resource(client_cls, client_params):
    client = client_cls(**client_params)
    resp = client.iter_list_resource(
        "fnlttSinglAcnt", {"corp_code": "00126380", "bsns_year": "2019", "reprt_code": "11011"}, timeout=3
    )
    items = [i for i in resp]

    assert isinstance(items, list)
    assert isinstance(items[0], dict)
