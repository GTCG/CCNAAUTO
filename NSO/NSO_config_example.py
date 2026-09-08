import json
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import quote

# -----------------------------
# NSO Connection Details
# -----------------------------
NSO_BASE_URL = "http://10.10.20.47:8080"
NSO_USERNAME = "developer"
NSO_PASSWORD = "C1sco12345"

# -----------------------------
# Loopback Details
# -----------------------------
LOOPBACK_ID = 99
LOOPBACK_DESCRIPTION = "Created by NSO API"

# -----------------------------
# Target IOS-XE Devices
# -----------------------------
TARGET_DEVICES = [
    {
        "device": "dist-rtr01",
        "ip_address": "10.10.20.175",
        "subnet_mask": "255.255.255.255",
    },
    {
        "device": "dev-dist-rtr01",
        "ip_address": "10.10.20.176",
        "subnet_mask": "255.255.255.255",
    },
]

# -----------------------------
# RESTCONF Headers
# -----------------------------
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def build_loopback_url(device_name):
    encoded_device_name = quote(device_name, safe="")
    return (
        f"{NSO_BASE_URL}/restconf/data/"
        f"tailf-ncs:devices/device={encoded_device_name}/"
        f"config/tailf-ned-cisco-ios:interface/"
        f"Loopback={LOOPBACK_ID}"
    )


def build_loopback_payload(ip_address, subnet_mask):
    return {
        "tailf-ned-cisco-ios:Loopback": [
            {
                "name": LOOPBACK_ID,
                "description": LOOPBACK_DESCRIPTION,
                "ip": {
                    "address": {
                        "primary": {
                            "address": ip_address,
                            "mask": subnet_mask,
                        }
                    }
                },
            }
        ]
    }


def create_loopback_on_device(device_info):
    device_name = device_info["device"]
    ip_address = device_info["ip_address"]
    subnet_mask = device_info["subnet_mask"]

    url = build_loopback_url(device_name)
    payload = build_loopback_payload(ip_address, subnet_mask)

    print("=" * 70)
    print(f"Creating Loopback{LOOPBACK_ID} on {device_name}")
    print("=" * 70)
    print(f"Device       : {device_name}")
    print(f"Loopback     : Loopback{LOOPBACK_ID}")
    print(f"IP Address   : {ip_address}")
    print(f"Subnet Mask  : {subnet_mask}")
    print(f"API Endpoint : {url}")
    print()

    response = requests.put(
        url,
        headers=HEADERS,
        auth=HTTPBasicAuth(NSO_USERNAME, NSO_PASSWORD),
        data=json.dumps(payload),
        timeout=30,
    )

    print(f"Status Code: {response.status_code}")

    if response.text:
        print("Response:")
        print(response.text)

    if response.status_code in [200, 201, 204]:
        print(f"SUCCESS: Loopback{LOOPBACK_ID} was created on {device_name}.")
        return True

    print(f"FAILED: Could not create Loopback{LOOPBACK_ID} on {device_name}.")
    return False


def main():
    print("=" * 70)
    print("Creating Loopback Interfaces via NSO RESTCONF API")
    print("=" * 70)
    print(f"NSO URL      : {NSO_BASE_URL}")
    print(f"Loopback ID  : {LOOPBACK_ID}")
    print(f"Description  : {LOOPBACK_DESCRIPTION}")
    print()

    success_count = 0
    for device_info in TARGET_DEVICES:
        if create_loopback_on_device(device_info):
            success_count += 1
        print()

    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total devices attempted : {len(TARGET_DEVICES)}")
    print(f"Successful changes      : {success_count}")
    print(f"Failed changes          : {len(TARGET_DEVICES) - success_count}")


if __name__ == "__main__":
    main()