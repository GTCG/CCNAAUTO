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
    membership_url = f"{BASE_URL}/dna/intent/api/v1/membership/{TARGET_SITE_ID}"
    membership_response= requests.get(
        membership_url,
        headers=headers,
        verify=False
    )
    if membership_response.status_code ==200:
        membership_data = membership_response.json()
        devices = membership_data.get("device",[])
        if devices and devices[0].get("response"):
            print ("\nDevices in site:\n")
            for device in devices[0]["response"]:
                print (f"hostname   : {device.get('hostname')}")
                print (f"management IP   : {device.get('managementIpAddress')}")
                print (f"Platform   : {device.get('platformId')}")
                print (f"Serial Number  : {device.get('serialNumber')}")
                print (f"reachability   : {device.get('reachabilityStatus')}")
                print("-" *50)
        else:
            print ("No devices found at this site.")
    else:
        print("failed to retrieve membership")
        print(membership_response.text)
else:
    print ("authentication failed")
    print(response.text)