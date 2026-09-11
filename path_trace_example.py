#disable or all lines by pressing control+/
#retrieve token
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import time
import json
urllib3.disable_warnings()

#BASE_URL = "https://sandboxdnac2.cisco.com"
BASE_URL= "https://sandboxdnac.cisco.com"
AUTH_URL = "/dna/system/api/v1/auth/token"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify = False)
#print(response.status_code)
#print(response.text)
token = response.json()["Token"]
headers = {"X-auth-token": token, "content-type": "application/json"}

# Get all IP-addresses and hostnames of the registered devices in Catalyst Center
headers = {"X-auth-token": token, "content-type": "application/json"}
DEVICES_URL = "/dna/intent/api/v1/network-device"
response = requests.get(BASE_URL + DEVICES_URL, headers=headers, verify=False)
devices= response.json()
print ("=== Registered devices in catalyst center: ===")
for device in devices["response"]:
    print ("IP: " + device["managementIpAddress"] + "," + "Hostname: " + device["hostname"])


# #determine source ip

headers = {"X-auth-token": token, "content-type": "application/json"}
DEVICES_URL = "/dna/intent/api/v1/network-device"
src_ip_address = ""
query_string_params = {'hostname': "sw1"}
response= requests.get(BASE_URL + DEVICES_URL, headers=headers, params=query_string_params, verify= False)
src_ip_address = response.json()["response"][0]["managementIpAddress"]
print ("IP source device: " + src_ip_address)

# #determine destination IP

headers = {"X-auth-token": token, "content-type": "application/json"}
DEVICES_URL = "/dna/intent/api/v1/network-device"
dst_ip_address = ""
query_string_params = {'hostname': "sw2"}
response= requests.get(BASE_URL + DEVICES_URL, headers=headers, params=query_string_params, verify= False)
dst_ip_address = response.json()["response"][0]["managementIpAddress"]
print ("Destination IP address: " + dst_ip_address)

#create path trace
PATH_TRACE_URL = "/dna/intent/api/v1/flow-analysis"
path_trace_payload = {
     "sourceIP":src_ip_address,
     "destIP": dst_ip_address,
     'inclusions': [
         "INTERFACE-STATS",
         "DEVICE-STATS",
         "ACL-TRACE",
         "QOS-STATS"
     ],
     "protocol": "icmp"
 }
response = requests.post(BASE_URL + PATH_TRACE_URL,headers=headers, json=path_trace_payload, verify= False)
flow_analysis_id = response.json()["response"]["flowAnalysisId"]
print ("Flow analysis ID: " + flow_analysis_id)

# #retrieve path trace through json. dumps(string)

time.sleep(5)
path_trace_id_URL = "/dna/intent/api/v1/flow-analysis/{flow_analysis_id}"
response = requests.get(BASE_URL + path_trace_id_URL.format(flow_analysis_id = flow_analysis_id), headers=headers, verify=False)
result = (response.json()["response"])
print(json.dumps(result, indent=2))
#delete path trace
response = requests.delete(BASE_URL + path_trace_id_URL.format(flow_analysis_id=flow_analysis_id),headers=headers, verify=False)
print(response)
