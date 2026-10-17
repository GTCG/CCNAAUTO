import json
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

VMANAGE_IP = "sandboxsdwan.cisco.com"
USERNAME= "devnetuser"
PASSWORD= "Cisco123!"

BASE_URL_STR = "https://{}:8443/".format (VMANAGE_IP)

LOGIN_ACTION = "j_security_check"
LOGIN_DATA = {"j_username": USERNAME, "j_password" : PASSWORD}


