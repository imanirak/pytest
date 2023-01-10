import pytest
from unittest.mock import Mock
from saml_data import SamlResponse
import requests
import json
import xmltodict
import pprint



@pytest.fixture
def saml_response():
    with open('xml_file') as f:
        doc = xmltodict.parse(f.read())

    for key,value in doc.items():
        print(key)
        print('--------------------------------')
        print(value)
        print('--------------------------------')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(doc))

    return SamlResponse()


def test_saml_get_response(saml_response):
    response = requests.get("")
    assert response.status_code == 200
    