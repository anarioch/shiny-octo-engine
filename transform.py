#!/bin/python3

import requests
import xml.etree.ElementTree as ET
import json

def transform(xmlText):
    xml = ET.fromstring(xmlText)
    # TODO: Add error handling to validate input format
    return {
        "id": xml.find("id").text,
        "name": xml.find("name").text,
        "description": xml.find("description").text,
    }

def process(id):
    # Fetch
    r = requests.get(f'https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/{id}.xml')
    if r.status_code != 200:
        print(f"Error: target API call failed with code '{r.status_code}'")
        return

    # Transform
    data = transform(r.text)

    # Output
    output = json.dumps(data)
    print(output)


if __name__ == "__main__":
    id = '1'
    process(id)