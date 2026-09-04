import requests
ip = requests.get('https://api.ipify.org').text
print (f"my IP address is {ip}")