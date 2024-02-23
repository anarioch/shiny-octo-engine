from django.http import HttpResponse

import requests
import xml.etree.ElementTree as ET
import json


# Transform the data from the source XML format into a Python object
def transform(xmlText):
    xml = ET.fromstring(xmlText)
    # TODO: Add error handling to validate input format
    return {
        "id": xml.find("id").text,
        "name": xml.find("name").text,
        "description": xml.find("description").text,
    }

# Return details about a company
def index(request, company_id):
    # Fetch
    r = requests.get(f'https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/{company_id}.xml')
    if r.status_code != 200:
        return HttpResponse(status=502, content=f"Error accessing backend API, received status code '{r.status_code}'")

    # Transform
    data = transform(r.text)

    # Output
    output = json.dumps(data)
    return HttpResponse(content_type="text/json", content=output)
