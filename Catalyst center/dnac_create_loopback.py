import requests
import json

requests.packages.urllib3.disable_warnings()

device_ip = '10.10.20.175'
username = 'cisco'
password = 'cisco'

url = f'https://{device_ip}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback'

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

payload = {
    "Cisco-IOS-XE-native:Loopback": [
        {
            "name": 100,
            "description": "Created via RESTCONF - CCNAAUTO test",
            "ip": {
                "address": {
                    "primary": {
                        "address": "192.168.100.1",
                        "mask": "255.255.255.0"
                    }
                }
            }
        }
    ]
}

response = requests.post(
    url,
    auth=(username, password),
    headers=headers,
    data=json.dumps(payload),
    verify=False
)

print(response.status_code)
print(response.text)