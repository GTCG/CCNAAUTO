""" print network ID"""


import requests
import json

networkID= "L_669910444571383872"
url = f"https://api.meraki.com/api/v1/networks/{networkID}"
bearer="df0a0671c3c409e8f0b88b6f5aaabd00c0a1dca6"

payload = None

headers = {
    "Authorization": f"Bearer {bearer}",
    "Accept": "application/json"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))
data = response.json()
print(data["id"])


