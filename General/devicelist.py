from classusage import Router, Switch

rtr1 = Router("iosV", "15.6.7", "10.10.10.1")
rtr2 = Router("iosV7", "15.7.7", "10.10.10.2")
sw1 = Switch("Cat9300", "16.9.5", "10.10.10.3")

print("rtr1\n", rtr1.getdesc(), '\n', sep='')
print("rtr2\n", rtr2.getdesc(), '\n', sep='')
print("sw1\n", sw1.getdesc(), '\n', sep='')