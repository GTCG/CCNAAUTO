"""Global parameters"""
WEBEX_TOKEN= "NTdjMGRiZTItYjU3My00YjdlLWE2YWEtM2FjNDJjMDNiODRlN2RlMTIyYTMtN2Vh_PE93_c8b056ff-2097-4f20-987c-5bdaeff74d03"
import json
import requests
url = "https://webexapis.com/v1/rooms/"



payload = {}
headers = {
  "Authorization":f"Bearer {WEBEX_TOKEN}",
  "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(json.dumps(response.json(), indent=2))
