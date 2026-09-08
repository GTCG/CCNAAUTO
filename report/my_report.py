from prettytable import PrettyTable

def print_report(report_name, devices):

    table = PrettyTable()
    table.field_names = ["Name", "Platform", "Management IP", "SW/FW version"]
    for device in devices:
        table.add_row(
            [device["hostname"],
            device["platform"],
            device["mgmt_ip"],
            device["version"]]
        )

    print(f"\n*** MY REPORT: {report_name} ***\n")
    print(table)


if __name__ == "__main__":
    report_name = "Catalyst Center managed devices"

    network_devices = [
        {
            "hostname": "rtr1",
            "family":"Routers",
            "platform": "C8200L-1N-4T",
            "mgmt_ip": "10.10.20.174",
            "version": "17.9.20220318:182713"
        },
        {
            "hostname": "sw1",
            "family":"Switches and Hubs",
            "platform": "C9KV-UADP-8P",
            "mgmt_ip": "10.10.20.175",
            "version": "17.9.20220318:182713"
        },
        {
            "hostname": "sw2",
            "family":"Switches and Hubs",
            "platform": "C9KV-UADP-8P",
            "mgmt_ip": "10.10.20.176",
            "version": "17.9.20220318:182713"
        }
    ]

    print_report(report_name, network_devices)