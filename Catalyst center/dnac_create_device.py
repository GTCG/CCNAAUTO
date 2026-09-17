"""Cisco Catalyst Center Lab The developer reserved the Lab and receives software VPN access
information via email at the start of the reservation. (For more information, see the next tab called
"VPN Access".) Once connected via software VPN, the developer can access the sandbox devices described below.
Sandbox Topology Information The Cisco Catalyst Center Sandbox consists of a virtualized
Controller and a virtualized sample network topology containing network elements and hosts that
developers can utilize for the duration of the reservation. Other Network Elements:
Refer to the Lab Topology Diagram
System Connection Information (After VPN Connection)
Cisco Catalyst-Center Controller:IP: 10.10.20.185 HTTPS: with credentials [administrator/Cisco1234!]
CML: IP: 10.10.20.161 HTTPS: with credentials [developer/C1sco12345]
CML 9kv Nodes: 10.10.20.175 -> 10.10.20.178 [cisco/cisco][no enable password required]
To add network device to Catalyst Center please use ip address of node, username and password and SNMP v2
RO community string name public.
ISE Server: IP: 10.10.20.25 HTTPS: with credentials [admin/Cisco1234!]
devbox Server: URL: http://10.10.20.50:8080/?folder=/home/developer/devbox-workspace HTTPS: with
credentials [C1sco12345]
devtools Server:

gitlab: http://10.10.20.54:8080/users/sign_in
admin credentials: [devadmin/C1sco12345]
user credentials: [developer/C1sco12345]
netbox: http://10.10.20.54:8000/login/?next=/
credentials:
postgres: 10.10.20.54
port: 5432
database: terraform
username: tfuser
password: TFisC00l
redis: 10.10.20.54
port: 6379
password: CICDRedisDevnet
Please note: Catalyst Center and ISE integration requires an active PXGrid connection. Please check and Add
PX-Grid service by going to System->Settings->External-Services->Authentication-Policy-Servers and edit ISE 
Server(10.10.20.25) and use admin credentials to Add ISE to Catalyst Center.

Additional Resources
Cisco Catalyst Center Hello World Example
Introduction to Cisco Catalyst Center REST APIs
Cisco Catalyst Center on DevNet
Sandbox Support"""

import requests
from requests.auth import HTTPBasicAuth
import json

requests.packages.urllib3.disable_warnings()

# Sandbox / target details
dnac_ip = "10.10.20.185"  
username = "administrator"
password = "Cisco1234!"


def get_token(dnac_ip, username, password):
    url = f'https://{dnac_ip}/dna/system/api/v1/auth/token'
    response = requests.post(
        url,
        auth=HTTPBasicAuth(username, password),
        verify=False
    )
    return response.json()['Token']


def add_device_to_dnac(dnac_ip, device_ip, snmp_version,
                        snmp_ro_community, snmp_rw_community,
                        snmp_retry, snmp_timeout,
                        cli_transport, username, password,
                        enable_password, token):

    device_object = {
        'ipAddress': [
            device_ip
        ],
        'type': 'NETWORK_DEVICE',
        'computeDevice': False,
        'snmpVersion': snmp_version,
        'snmpROCommunity': snmp_ro_community,
        'snmpRWCommunity': snmp_rw_community,
        'snmpRetry': snmp_retry,
        'snmpTimeout': snmp_timeout,
        'cliTransport': cli_transport,
        'userName': username,
        'password': password,
        'enablePassword': enable_password
    }

    response = requests.post(
        'https://{}/dna/intent/api/v1/network-device'.format(dnac_ip),
        data=json.dumps(device_object),
        headers={
            'X-Auth-Token': '{}'.format(token),
            'Content-type': 'application/json'
        },
        verify=False
    )
    return response.json()


# --- Run it ---

token = get_token(dnac_ip, username, password)
print (token)

result = add_device_to_dnac(
    dnac_ip=dnac_ip,
    device_ip='10.10.20.175',      
    snmp_version='v2',
    snmp_ro_community='public',
    snmp_rw_community='public',
    snmp_retry=3,
    snmp_timeout=5,
    cli_transport='ssh',
    username='cisco', 
    password='cisco',
    enable_password='',
    token=token
)
print(result)

task_url = f"https://{dnac_ip}{result['response']['url']}"
task_response = requests.get(
    task_url,
    headers={'X-Auth-Token': token},
    verify=False
)
print(task_response.json())
print("Status code:", task_response.status_code)