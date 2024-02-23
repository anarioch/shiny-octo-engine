#!/bin/python3

# This is a simple CLI app to invoke the transform against the remote MWNZ sample API.
#
# Example invocations:
# $ ./transform.py 1
# {"id": "1", "name": "MWNZ", "description": "..is awesome"}
# $ ./transform.py 4
# Error: target API call failed with code '404'


import argparse
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


def main():
    parser = argparse.ArgumentParser(description="Return company details")
    parser.add_argument('company_id', type=int, help="The company to look up")

    args = parser.parse_args()

    process(args.company_id)

if __name__ == "__main__":
    main()
