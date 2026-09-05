import my_report
import catalyst_devices
import meraki_devices

catalyst_report_name = "Catalyst center managed devices"
catalyst_url = "https://sandboxdnac.cisco.com"
catalyst_username = "devnetuser"
catalyst_password = "Cisco123!"

meraki_report_name = "Catalyst center managed devices"
meraki_password = "Cisco123!"
meraki_org ="669910444571369742"

catalyst_token= catalyst_devices.get_catalyst_center_token
catalyst_devices = catalyst_devices.get_catalyst_center_devices
meraki_switches = meraki_devices.get_meraki_switches

my_report.print_report(catalyst_report_name, catalyst_devices)
my_report.print_report(meraki_report_name, meraki_switches)



