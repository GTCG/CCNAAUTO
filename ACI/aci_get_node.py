import os
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
APIC_URL = "https://10.10.20.14"
USERNAME= "admin"
PASSWORD = "Cisco12345"
#create session
session=requests.Session()
session.verify = False
login_url=f"{APIC_URL}/api/aaaLogin.json"
login_payload= {
    "aaaUser": {
        "attributes": {
            "name": USERNAME,
            "pwd": PASSWORD
        }
    }
}
login_response = session.post(login_url, json=login_payload)
if login_response.status_code!= 200:
    print("authentication failed")
    print(login_response.text)
    exit(1)
print ("authentication succesful")
devices_url = f"{APIC_URL}/api/node/class/fabricNode.json"
devices_response = session.get(devices_url)
if devices_response.status_code  !=200:
    print ("failed to retrieve fabric devices")
    print (devices_response.text)
    exit(1)
devices = devices_response.json().get("imdata",[])
print ("\nACI fabric devices:\n")
for item in devices:
    attributes = item["fabricNode"]["attributes"]
    print(f"Name:       {attributes.get('name')}")
    print(f"Node ID:       {attributes.get('id')}")
    print(f"Role:       {attributes.get('role')}")
    print(f"Model:       {attributes.get('model')}")
    print(f"Serial:       {attributes.get('serial')}")
    print(f"POD id:       {attributes.get('podId')}")
    print(f"State:       {attributes.get('fabricSt')}")
    print("-" * 50)

    