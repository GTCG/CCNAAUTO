import json
import requests
import urllib3

# Zelfondertekend certificaat in het lab: onderdruk de waarschuwing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "192.168.110.50"
RESTCONF_PORT = 443
USERNAME = "admin"
PASSWORD = "admin"

URL = f"https://{HOST}:{RESTCONF_PORT}/restconf/data/ietf-interfaces:interfaces"

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def main():
    try:
        response = requests.get(
            URL,
            auth=(USERNAME, PASSWORD),
            headers=HEADERS,
            verify=False,
            timeout=30,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP fout: {e}")
        print(response.text)
        return
    except requests.exceptions.RequestException as e:
        print(f"Verbindingsfout: {e}")
        return
    print (f"GET gelukt: HTTP {response.status_code} {response.reason}")

    data = response.json()
    result = json.dumps(data, indent=2)
    print(result)

if __name__ == "__main__":
    main()