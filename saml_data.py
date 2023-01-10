import json
import xmltodict
import pprint



with open('saml_test_data.xml') as f:
    doc = xmltodict.parse(f.read())
    print(type(doc))

    for key,value in doc.items():
        print(key)
        print('--------------------------------')
        print(value)
        print('--------------------------------')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(doc))


#what we want the response to do
class SamlResponse:
    def __init__(self):
        pass
    
    def get(self):
        pass
    
    def post(self):
        pass
