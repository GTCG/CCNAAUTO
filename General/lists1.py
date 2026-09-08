my_interfaces = ["gigabitethernet 1", "gigabitethernet 2","gigabitethernet3"]
my_interfaces.append([24, True, "Default gateway"])
#print (my_interfaces[3][1])
device_details= {"hostname": "sw1", "sw_version": 20.4, "alerts": "False"}
#print(device_details["hostname"])
device_details["interfaces"] = my_interfaces
#print (device_details)
print (device_details["interfaces"][3][2])