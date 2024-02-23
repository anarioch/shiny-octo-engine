#!/bin/python3

import requests
import xml.etree.ElementTree as ET
import json

def process(id):
    r = requests.get(f'https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/{id}.xml')
    if r.status_code != 200:
        print(f"Error: target API call failed with code '{r.status_code}'")
        return
    
    xml = ET.fromstring(r.text)
    data = {
        "id": xml.find("id").text,
        "name": xml.find("name").text,
        "description": xml.find("description").text,
    }

    output = json.dumps(data)
    print(output)

if __name__ == "__main__":
    id = '1'
    process(id)