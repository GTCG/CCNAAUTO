import requests
import urllib3

urllib3.disable_warnings()

def get_catalyst_center_token(username:str, password:str, url:str)->str:
    """
    A function to retrieve Catalyst Center authorization token.

    Args:
        username (str) : Username used for authentication.
        password (str) : Password used for authentication
        url (str): The URL of your Catalyst center

    Returns:
        The authorization token as a string.
    """

    url = f"{url}/dna/system/api/v1/auth/token"

    response = requests.request("POST", url, auth=(username, password), verify=False)
    token = response.json()["Token"]
    return token

def get_catalyst_center_devices(token:str, url:str)->list:
    """
    A function to retrieve Catalyst Center managed switches.

    Args:
        token (str) : Catalyst Center token to authorize the API call
        url (str): The URL of your Catalyst center

    Returns:
        A list of dictionaries representing all the devices found in the network, in the correct
        format to be used with print_report function
    """

    url = f"{url}/dna/intent/api/v1/network-device"
    headers = {'x-auth-token': token}
    response = requests.request("GET", url, headers=headers, verify=False)

    devices = response.json()["response"]
    report_devices = []

    for device in devices:
        report_devices.append({
            "hostname": device["hostname"],
            "platform": device["platformId"],
            "mgmt_ip": device["managementIpAddress"],
            "version": device["softwareVersion"]
        })

    return report_devices