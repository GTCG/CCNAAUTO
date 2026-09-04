""" print devices"""


import requests1
import json

networkID= "L_669910444571383872"
baseUrl= "https://api.meraki.com/api/v1"
url = f"{baseUrl}/networks/{networkID}/devices"
bearer="df0a0671c3c409e8f0b88b6f5aaabd00c0a1dca6"

payload = None

headers = {
    "Authorization": f"Bearer {bearer}",
    "Accept": "application/json"
}

response = requests1.request('GET', url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
data = response.json()
print (data)
print("Model: ", data[0]["model"])
print ("Latitude: ",data[0]["lat"])
print ("serial: ",data[0]["serial"])
