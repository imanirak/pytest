import pytest
from unittest.mock import Mock
from saml_data import SamlResponse

@pytest.fixture
def response():
    return SamlResponse("saml_test_data.xml")

# tested failure and success returns 
def test_find_certificate(response):
    if response.verify_certificate() is None:
        assert False
    else:
        assert True

# tested failure and success returns 
def test_find_signature(response):
    if response.verify_signature() is None:  
        assert False
    else:
        assert True

# tested failure and success returns 
def test_verify_status(response):
    status = response.saml2p_status_code()
   # success_status = 'urn:oasis:names:tc:SAML:2.0:status:Success'
    if not 'Success' in status:
       assert False
    else:
        assert True
    
    