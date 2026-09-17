
import requests
import my_report
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'X-Auth-Token': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY3RpdmVSRCI6IjliZjZiMjViMGM1ZTQwM2Q1MTc5ZmM5ZDQxZDViYWQ0ZjM4N2RjNDUiLCJhdWQiOiJDRE5BIiwiYXV0aFNvdXJjZSI6ImxlZ2FjeSIsImNsaWVudElkIjoiZGV2bmV0dXNlciIsImVtYWlsIjoiZGV2bmV0dXNlckBsb2NhbHVzZXIuY29tIiwiZXhwIjoxNzg1NDg0MzQ2LCJmaXJzdE5hbWUiOiJkZXZuZXR1c2VyIiwiaWF0IjoxNzg1NDgwNzQ2LCJpc3MiOiJkbmFjIiwicmRzIjpbIjliZjZiMjViMGM1ZTQwM2Q1MTc5ZmM5ZDQxZDViYWQ0ZjM4N2RjNDUiXSwicmVzb3VyY2VHcm91cHMiOiJINHNJQUFBQUFBQUEvNHF1VmlvdVNnNUtMYzR2TFVwTzlVeFJzbExTVXRKUktxa3NTRld5VWlyT0xFbFZxbzBGQkFBQS8vK2N2WGZLSlFBQUFBPT0iLCJyb2xlcyI6WyJPQlNFUlZFUiJdLCJzZXNzaW9uSWQiOiI2MGQ1OTlkOC1iOTEzLTU4ODQtOTEzOS0wOTYwMTg3NDZiYTAiLCJzdWIiOiI2OTM5OTU5OWJiNWE2YjAwNTA3YTcwMTAiLCJ0ZW5hbnRJZCI6IjY3YjkzNWM1OTE1NWY1MDAxMzUxNWQxYyIsInRlbmFudE5hbWUiOiJUTlQwIiwidXNlcm5hbWUiOiJkZXZuZXR1c2VyIn0.szvbfotVaIhEsuX1oJJY5bo3aXxir1NVWw78fhVeFp4E648ugF_d8KYmDjnNyoMFI0MX54JWWPuHsxTeEAXSxQ',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, auth=("devnetuser", "Cisco123!"), verify=False)

my_token = response.json()["Token"]
#print (my_token)

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
headers= {
    'X-auth-token': my_token
}

response= requests.request("Get", url, headers=headers, verify=False)
Devices=response.json()["response"]
report_devices=[]
for device in Devices:
    #print("my device")
    #print(device["hostname"])
    #print(device["platformId"])
    #print(device["managementIpAddress"])
    #print(device["softwareVersion"])
    report_devices.append({
    "hostname": device["hostname"], #use the same column names as defined in my_report. The script will look for these names and fill in the data from device[]
    "platform": device["platformId"],
    "mgmt_ip" :device["managementIpAddress"],
    "version":device["softwareVersion"]
    })
report_name = "Catalyst Center managed devices"
my_report.print_report(report_name, report_devices )




