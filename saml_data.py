import json
import xmltodict
from typing import List
import pprint

class SamlResponse:
    #convert xml to dict
    def __init__(self, doc: str) -> None:
        with open(doc) as f:
            self.doc = xmltodict.parse(f.read())
            
    # verify certificate has been found       
    def verify_certificate(self):
        doc = self.doc
        for i in doc.items():
            cert = doc["saml2p:Response"]["ds:Signature"]["ds:KeyInfo"]["ds:X509Data"]["ds:X509Certificate"]
        return cert
    
    def verify_signature(self):
        doc = self.doc
        for i in doc.items():
            sig = doc["saml2p:Response"]["ds:Signature"]["ds:SignatureValue"]
        return sig
        
    def saml2p_status_code(self):
        # verify success status
        doc = self.doc
        for i in doc.items():
            status = doc["saml2p:Response"]["saml2p:Status"]["saml2p:StatusCode"]["@Value"]
            
        return status

test = SamlResponse("saml_test_data.xml")
# print(test.verify_certificate())
# print(test.verify_signature())
print(test.saml2p_status_code())

# with open("saml_test_data.xml") as f:
#     doc = xmltodict.parse(f.read())
#     for i in doc.items():
#         certificate_info = doc["saml2p:Response"]["saml2p:Status"]["saml2p:StatusCode"]["@Value"]
#         certificate_info.find("Success")
#         print(certificate_info)