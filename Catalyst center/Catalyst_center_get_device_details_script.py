from API_KEY import Catalyst_username
from API_KEY import Catalyst_password
import requests
import json
import os
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
#disable SSL warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
BASE_URL= "https://sandboxdnac.cisco.com"
USERNAME= Catalyst_username
PASSWORD = Catalyst_password
TARGET_SITE_ID="00f6df3f-c067-4d55-8ff3-059d35bbaa0c"
DEVICE_ID= "aa754801-8895-41e8-8ca5-27ee415c9c42"

#get authentication token
auth_url=f"{BASE_URL}/dna/system/api/v1/auth/token"
response = requests.post(
    auth_url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)
print (response)

if response.status_code == 200:
    Token = response.json()["Token"]
    headers = {
        "X-Auth-token": Token,
        "content-type": "application/json"
    }
    device_url=f"{BASE_URL}/dna/intent/api/v1/network-device/{DEVICE_ID}"

    device_response= requests.get(
        device_url,
        headers=headers,
        verify=False
    )

    if device_response.status_code == 200:
        device=device_response.json()["response"]
        print("\nDevice Details:\n")

        print (f"Hostname:          {device.get('hostname')}")
        print (f"Management IP:     {device.get('managementIpAddress')}")
        print (f"Platform:          {device.get('platformId')}")
        print (f"Software version:  {device.get('softwareVersion')}")
        print (f"Serial Number:     {device.get('serialNumber')}")
        print (f"Reachability:      {device.get('reachabilityStatus')}")
        print (f"Family:            {device.get('family')}")
        print (f"Role:              {device.get('role')}")
    else:
        print("failed to retrieve device information")
        print(device_response.text)
else:
    print("authentication failed")
    print(response.text)