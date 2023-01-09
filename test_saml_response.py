import pytest
from unittest.mock import Mock
from saml_data import SamlResponse
import requests

@pytest.fixture
def saml_response():
    return SamlResponse()


def test_saml_get_response(saml_response):
    response = requests.get("")
    assert response.status_code == 200
    