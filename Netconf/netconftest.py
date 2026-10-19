from ncclient import manager
import paramiko
import logging
#print(paramiko.Transport._preferred_keys)
#print("ssh-rsa" in paramiko.Transport._key_info)
#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger("paramiko").setLevel(logging.DEBUG)




IOSXR_HOST = "192.168.110.50"
NETCONF_PORT = 830
RESTCONF_PORT = 443
SSH_PORT = 22
GNMI_PORT = 57777
USERNAME = "admin"
PASSWORD = "admin"

def get_capabilities():
    with manager.connect(
        host= IOSXR_HOST,
        port = NETCONF_PORT,
        username = USERNAME,
        password = PASSWORD,
        hostkey_verify = False,
        ) as device:

        print ('\n**NETCONF capabilities for device {}**\n'.format(IOSXR_HOST))
        for capability in device.server_capabilities:
            print(capability)


if __name__ == '__main__':
    get_capabilities()