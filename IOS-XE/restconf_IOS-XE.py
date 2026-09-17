"""
RESTCONF example against an IOS-XE device.

Requirements:
    pip install requests

Before running:
    - RESTCONF must be enabled on the device:
        conf t
        restconf
        interface <mgmt-if>
        ip http secure-server        (RESTCONF rides on HTTPS)
        ip http authentication local   (or aaa)
        end
    - Set credentials via environment variables (avoid hardcoding):
        $env:RESTCONF_HOST="192.168.1.1"
        $env:RESTCONF_USER="admin"
        $env:RESTCONF_PASS="yourpassword"
"""

import os
import json
import requests
import urllib3

# Self-signed certs on lab devices -> suppress the warning (don't do this in prod)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("RESTCONF_HOST", "192.168.110.160")
USER = os.environ.get("RESTCONF_USER", "admin")
PASS = os.environ.get("RESTCONF_PASS", "Cisco123!")

BASE_URL = f"https://{HOST}/restconf/data"

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def get_interfaces():
    """GET: show all interface configuration (ietf-interfaces model)."""
    url = f"{BASE_URL}/ietf-interfaces:interfaces"
    resp = requests.get(
        url, auth=(USER, PASS), headers=HEADERS, verify=False
    )
    resp.raise_for_status()  # raises before .json() if status is 4xx/5xx
    return resp.json()

def create_loopback(number, ip_address, netmask, description=""):
    """
    PUT: create (or replace) a Loopback interface using the native
    IOS-XE YANG model. PUT is used here rather than POST because we're
    targeting the exact resource URI (Loopback=<number>).
    """
    url = f"{BASE_URL}/Cisco-IOS-XE-native:native/interface/Loopback={number}"
    payload = {
        "Cisco-IOS-XE-native:Loopback": {
            "name": number,
            "description": description,
            "ip": {
                "address": {
                    "primary": {
                        "address": ip_address,
                        "mask": netmask
                    }
                }
            }
        }
    }
    resp = requests.put(
        url, auth=(USER, PASS), headers=HEADERS,
        data=json.dumps(payload), verify=False
    )
    resp.raise_for_status()
    status=resp.status_code
    print (status)
    return resp.status_code  # 201 Created or 204 No Content


create_loopback("300","192.168.1.10","255.255.255.0","testloopback")



def get_interface(name):
    """GET: show a single interface, e.g. name='GigabitEthernet2'."""
    url = f"{BASE_URL}/ietf-interfaces:interfaces/interface={name}"
    resp = requests.get(
        url, auth=(USER, PASS), headers=HEADERS, verify=False
    )
    resp.raise_for_status()
    return resp.json()


def set_interface_description(name, description):
    """
    PATCH: modify just the description of an existing interface.
    PATCH merges with existing config (doesn't require a full body,
    unlike PUT which replaces the entire resource).
    """
    url = f"{BASE_URL}/ietf-interfaces:interfaces/interface={name}"
    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": description,
        }
    }
    resp = requests.patch(
        url, auth=(USER, PASS), headers=HEADERS,
        data=json.dumps(payload), verify=False
    )
    resp.raise_for_status()
    return resp.status_code  # 204 No Content = success, no body returned

set_interface_description("GigabitEthernet1", "test")

def shutdown_interface(name, shutdown=False):
    """
    PATCH: enable/disable an interface.
    'enabled': false -> shutdown, 'enabled': true -> no shutdown.
    """
    url = f"{BASE_URL}/ietf-interfaces:interfaces/interface={name}"
    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "enabled": not shutdown,
        }
    }
    resp = requests.patch(
        url, auth=(USER, PASS), headers=HEADERS,
        data=json.dumps(payload), verify=False
    )
    resp.raise_for_status()
    return resp.status_code
shutdown_interface("GigabitEthernet4")

if __name__ == "__main__":
    # --- Example: read all interfaces ---
    data = get_interfaces()
    for intf in data["ietf-interfaces:interfaces"]["interface"]:
        print(f"{intf['name']}: enabled={intf.get('enabled')}, "
              f"description={intf.get('description', '')}")

    # --- Example: modify a description ---
    # status = set_interface_description("GigabitEthernet2", "Set via RESTCONF")
    # print("PATCH status:", status)

    # --- Example: shut/no shut an interface ---
    # status = shutdown_interface("GigabitEthernet3", shutdown=True)
    # print("PATCH status:", status)