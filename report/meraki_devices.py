import requests

def get_meraki_switches(token:str, organization_id:str)->list:
    """
    A function to retrieve Meraki managed switches.

    Args:
        token (str) : Meraki bearer token to authorize the API call
        organization_id (str): The ID of the Meraki organization whose switches are queried

    Returns:
        A list of dictionaries representing all the switches found in the organization, in the
        correct format to be used with print_report function
    """

    url = f"https://api.meraki.com/api/v1/organizations/{organization_id}/devices"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.request('GET', url, headers=headers)
    devices = response.json()
    switches = []
    for device in devices:
        if device["productType"] == "switch":
            switches.append({
                "hostname": device["mac"],
                "platform": device["model"],
                "mgmt_ip": device["lanIp"],
                "version": device["firmware"]
            })
    return switches