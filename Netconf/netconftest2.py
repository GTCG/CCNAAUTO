from ncclient import manager
from ncclient.operations import RPCError

HOST = "192.168.110.50"
NETCONF_PORT = 830
USERNAME = "admin"
PASSWORD = "admin"

LOOPBACK_ID = 100
DESCRIPTION = "Created via NETCONF"
IP_ADDRESS = "10.10.10.1"
NETMASK = "255.255.255.255"

# Cisco-IOS-XE-native model: dit is het model dat het dichtst bij de CLI ligt
CONFIG = f"""
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>{LOOPBACK_ID}</name>
        <description>{DESCRIPTION}</description>
        <ip>
          <address>
            <primary>
              <address>{IP_ADDRESS}</address>
              <mask>{NETMASK}</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Filter om de loopback terug te lezen
FILTER = f"""
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>{LOOPBACK_ID}</name>
      </Loopback>
    </interface>
  </native>
"""


def main():
    with manager.connect(
        host=HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False,
        device_params={"name": "iosxe"},
        timeout=60,
    ) as m:
        try:
            reply = m.edit_config(target="running", config=CONFIG)
            print(f"Loopback{LOOPBACK_ID} aangemaakt:", "OK" if reply.ok else "FOUT")
        except RPCError as e:
            print("NETCONF fout bij edit_config:", e)
            return

        print("\nControle (get_config):\n")
        print(m.get_config(source="running", filter=("subtree", FILTER)).data_xml)


if __name__ == "__main__":
    main()