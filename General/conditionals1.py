device_details = {"hostname": "sw1", "sw_version": 20.4, "alerts": False, "interfaces": ["GigabitEthernet 1", "GigabitEthernet 2", "GigabitEthernet 3"]}
if device_details["alerts"] == True:
    print("There are alerts on the device")
else:
    print("There are no alerts on this device")
if "GigabitEthernet 2" in device_details["interfaces"]:
    print("GigabitEthernet2 is on this device!")
elif "GigabitEthernet 2" in device_details["interfaces"]:
    print("GigabitEthernet3 is on this device!")

for interface in device_details["interfaces"]:
    print (interface)

while True:
    results_available= input("Are there rest results available?").lower()
    if results_available == "yes":
        print("results are available")
        break
    else:
        print ("results are not available yet")
