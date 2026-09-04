from prettytable import PrettyTable

report_name = "Catalyst center managed devices"
print (f"***My report: {report_name}***")

network_devices = [
    {
        "hostname": "rtr1",
        "Family": "routers",
        "Platform": "C8200L-1N-4T",
        "mgmt_ip": "10.10.20.174",
        "version": "17.9.20220318:182713"
    },
    {
        "hostname": "sw1",
        "Family": "switches and hubs",
        "Platform": "C9KV-UADP-8P",
        "mgmt_ip": "10.10.20.175",
        "version": "17.9.202203218:182713"
    },
    {
        "hostname": "sw2",
        "Family": "switches and hubs",
        "Platform": "C9KV-UADP-8P",
        "mgmt_ip": "10.10.20.176",
        "version": "17.9.202203218:182713" 
    }
]

#print(network_devices[1]["mgmt_ip"])
#print(network_devices[0]["Platform"])
#print(f"{network_devices[0]["hostname"]}, {network_devices[0]["Platform"]}, {network_devices[0]["mgmt_ip"]}, {network_devices[0]["version"]}")
#print(f"{network_devices[1]["hostname"]}, {network_devices[1]["Platform"]}, {network_devices[1]["mgmt_ip"]}, {network_devices[1]["version"]}")
#print(f"{network_devices[2]["hostname"]}, {network_devices[2]["Platform"]}, {network_devices[2]["mgmt_ip"]}, {network_devices[2]["version"]}")
table= PrettyTable()
table.field_names = ["Name", "Platform", "Management IP", "SW/FW version"]
for device in network_devices:
    table.add_row([device["hostname"], device['Platform'], device["mgmt_ip"], device["version"]])
print (table)