import xmltodict

class SamlResponse:
    #convert xml to dict
    def __init__(self, doc: str) -> None:
        with open(doc) as f:
            self.doc = xmltodict.parse(f.read())
            
    # verify certificate is present in response     
    def verify_certificate(self):
        doc = self.doc
        cert = doc["saml2p:Response"]["ds:Signature"]["ds:KeyInfo"]["ds:X509Data"]["ds:X509Certificate"]
        return cert
    
    # verify signature is present in response
    def verify_signature(self):
        doc = self.doc
        sig = doc["saml2p:Response"]["ds:Signature"]["ds:SignatureValue"]
        return sig
    
    # verify success status    
    def saml2p_status_code(self):
        doc = self.doc
        status = doc["saml2p:Response"]["saml2p:Status"]["saml2p:StatusCode"]["@Value"]  
        return status

test = SamlResponse("saml_test_data.xml")
print(test.doc)
# print(test.verify_certificate())
# print(test.saml2p_status_code())
# print(test.verify_signature())