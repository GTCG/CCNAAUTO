from API_KEY import Catalyst_username
from API_KEY import Catalyst_password
import requests1
import json
import os
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
#disable SSL warnings
requests1.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
BASE_URL= "https://sandboxdnac.cisco.com"
USERNAME= Catalyst_username
PASSWORD = Catalyst_password

#get authentication token
auth_url=f"{BASE_URL}/dna/system/api/v1/auth/token"
response = requests1.post(
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
    sites_url = f"{BASE_URL}/dna/intent/api/v1/site"
    sites_response = requests1.get(
        sites_url,
        headers = headers,
        verify = False
    )
    if sites_response.status_code == 200:
        sites = sites_response.json()["response"]
        print ("\nList of Sites:\n")
        for site in sites:
            print (f"Site name : {site.get("name")}")
            print (f"Site ID: {site.get("id")}")
            print ("-"*50)
    else:
        print ("failed to retrieve sites")
        print(sites_response.text)
else:
    print ("Authentication failed")
    print (response.text)


