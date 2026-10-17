import os
import sys
import requests

BASE_URL = "https://api.meraki.com/api/v1"
API_KEY = os.environ.get("MERAKI_KEY")
ORG_ID = "1788473"
NETWORK_ID = "L_646266546527669457"

if not API_KEY:
    sys.exit("Zet eerst de key: set MERAKI_KEY=jouwkey")

session = requests.Session()
session.headers.update({
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Accept": "application/json",
})


def get_all(path, params=None):
    """GET met automatische paginering via de Link-header."""
    url = f"{BASE_URL}{path}"
    results = []
    while url:
        r = session.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        results.extend(data if isinstance(data, list) else [data])
        url = r.links.get("next", {}).get("url")
        params = None  # next-URL bevat de parameters al
    return results


# 1. Organisaties
print("== Organisaties ==")
for org in get_all("/organizations"):
    print(f"{org['id']:>12}  {org['name']}")

# 2. Networks van de organisatie
print(f"\n== Networks in org {ORG_ID} ==")
for net in get_all(f"/organizations/{ORG_ID}/networks"):
    print(f"{net['id']:<25}  {net['name']}  {net.get('productTypes', [])}")

# 3. Devices van het network
print(f"\n== Devices in network {NETWORK_ID} ==")
for dev in get_all(f"/networks/{NETWORK_ID}/devices"):
    print(
        f"{dev.get('serial', '-'):<16} "
        f"{dev.get('model', '-'):<12} "
        f"{dev.get('name') or '(geen naam)':<30} "
        f"{dev.get('lanIp') or '-':<15} "
        f"{dev.get('mac', '-')}"
    )