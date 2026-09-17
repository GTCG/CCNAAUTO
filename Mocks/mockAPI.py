"""Fictional API: NetOps Inventory API

Base URL: https://10.10.20.50

1. Authentication
POST /netops/api/v1/auth/token
Send Basic Auth (username/password) in the request. Response body (JSON):

json
{"authToken": "a1b2c3d4e5"}

Token must be sent on all subsequent calls in header X-Netops-Token. Token lifetime: 30 minutes. Expired token → 401.

2. List devices
GET /netops/api/v1/devices
Optional query param: family (e.g. switches)
Response body (JSON):

json
{
  "response": [
    {"hostname": "sw1", "reachability": "Reachable", "serial": "FCW111"},
    {"hostname": "sw2", "reachability": "Unreachable", "serial": "FCW222"}
  ],
  "totalCount": 2
}"""

import requests
from requests.auth import HTTPBasicAuth
BASE_URL = "https://10.10.20.50"
AUTH_URL = "/netops/api/v1/auth/token"
DEVICES_URL = "/netops/api/v1/devices"
USERNAME = "admin"
PASSWORD = "C1sco12345"
TOKEN = "a1b2c3d4e5" #value: [authtoken]

def get_token():
    response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify= False)
    data= response.json()
    return data["authToken"]

def get_devices(token):
    headers = {"X-Netops-Token":token}
    response = requests.get(BASE_URL + DEVICES_URL, headers=headers, params={"family":"switches"}, verify= False)

    if response.status_code == 200:
        devices = response.json()["response"]
        for device in devices:
            print (f"{device['hostname']} - {device['reachability']}")
    else:
        print (f"error: {response.status_code}")


token = get_token()
get_devices(token)
