import yaml

# Single YAML document
with open('switches.yaml', 'r') as f:
    data = yaml.safe_load(f)

#print(data)
#print(data["devices"][0])
#print(data["devices"][0]["ip"])
#print(data["devices"][0]["role"])

for device in data["devices"]:
    print(device["ip"])
