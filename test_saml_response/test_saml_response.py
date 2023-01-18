import pytest
from saml_data import SamlResponse

@pytest.fixture
def response():
    return SamlResponse("saml_test_success.xml")

@pytest.fixture
def fresponse():
    return SamlResponse("saml_test_failure.xml")

class TestSuccess:
    def test_find_certificate(self, response):
        assert response.verify_certificate() is not None

    def test_find_signature(self, response):
        assert response.verify_signature() is not None

    def test_verify_status(self, response):
        status = response.saml2p_status_code()
        assert 'Success' in status

class TestFailure:
    def test_find_certificate(self, fresponse):
        assert fresponse.verify_certificate() is None

    def test_find_signature(self, fresponse):
        assert fresponse.verify_signature() is None

    def test_verify_status(self, fresponse):
        status = fresponse.saml2p_status_code()
        value = status.replace('Success', '')
        assert value not in ('Requester', 'Responder', 'VersionMismatch',
          'AuthnFailed', 'InvalidAttrNameOrValue')