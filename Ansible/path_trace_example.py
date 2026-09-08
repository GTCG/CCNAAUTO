#retrieve token
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

BASE_URL = "https://sandboxdnac2.cisco.com"
AUTH_URL = "/dna/system/api/v1/auth/token"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify = False)
#print(response.status_code)
#print(response.text)
token = response.json()["Token"]
headers = {"X-auth-token": token, "content-type": "application/json"}

# Get all hostnames
headers = {"X-auth-token": token, "content-type": "application/json"}
DEVICES_URL = "/dna/intent/api/v1/network-device"
response = requests.get(BASE_URL + DEVICES_URL, headers=headers, verify=False)
devices= response.json()
print(devices)

# #determine source ip

# headers = {"X-auth-token": token, "content-type": "application/json"}
# DEVICES_URL = "/dna/intent/api/v1/network-device"
# src_ip_address = ""
# query_string_params = {'hostname': "CSR1Kv-01.boson.com"}
# response= requests.get(BASE_URL + DEVICES_URL, headers=headers, params=query_string_params, verify= False)
# src_ip_address = response.json()["response"][0]["managementIpAddress"]

# #determine destination IP

# headers = {"X-auth-token": token, "content-type": "application/json"}
# DEVICES_URL = "/dna/intent/api/v1/network-device"
# dst_ip_address = ""
# query_string_params = {'hostname': "CSR1Kv-02.boson.com"}
# response= requests.get(BASE_URL + DEVICES_URL, headers=headers, params=query_string_params, verify= False)
# dst_ip_address = response.json()["response"][0]["managementIpAddress"]

# #create path trace
# PATH_TRACE_URL = "/dna/intent/api/v1/flow-analysis"
# path_trace_payload = {
#     "sourceIP":src_ip_address,
#     "destIP": dst_ip_address,
#     'inclusions': [
#         "INTERFACE-STATS",
#         "DEVICE-STATS",
#         "ACL-TRACE",
#         "QOS-STATS"
#     ],
#     "protocol": "icmp"
# }
# response = requests.post(BASE_URL + PATH_TRACE_URL,headers=headers, json=path_trace_payload, verify= False)
# flow_analysis_id = response.json()["response"]["flowAnalysisID"]

# #retrieve path trace

# path_trace_id_URL = "/dna/intent/api/v1/flow-analysis/{flow_analysis_id}"
# response = requests.get(BASE_URL + path_trace_id_URL.format(flow_analysis_id = flow_analysis_id), headers=headers, verify=False)
# print (response.json()["response"])

# #delete path trace
# response = requests.delete(BASE_URL + path_trace_id_URL.format(flow_analysis_id=flow_analysis_id),headers=headers, verify=False)
