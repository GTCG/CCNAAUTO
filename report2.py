from prettytable import prettytable
table = prettytable()
table.field_names = ["Name", "Platform", "Management IP", "SW/FW version"]
table.add_row(["sw1", "C9VK-UADP-8P", "10.10.20.175", "17.9.20220318:182713"])
table.add_row(["sw2", "C9VK-UADP-8P", "10.10.20.176", "17.9.20220318:182713"])