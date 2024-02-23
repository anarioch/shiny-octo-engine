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
def company(request, company_id):
    # Fetch
    r = requests.get(f'https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/{company_id}.xml')
    if r.status_code != 200:
        error_detail = {"error": "Resource not found", "error_description": f"No company found for ID '{company_id}'"}
        return HttpResponse(status=404, content=json.dumps(error_detail, indent=4))

    # Transform
    data = transform(r.text)

    # Output
    output = json.dumps(data)
    return HttpResponse(content_type="text/json", content=output)
