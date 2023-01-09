import json
import xmltodict
import pprint



def convert_xml_to_json(xml_file):   
    with open('xml_file') as f:
        doc = xmltodict.parse(f.read())
        print(type(doc))

    for key,value in doc.items():
        print(key)
        print('--------------------------------')
        print(value)
        print('--------------------------------')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(doc))



class SamlResponse:
    def __init__(self):
        pass
    
    def get(self):
        pass
    
    def post(self):
        pass
