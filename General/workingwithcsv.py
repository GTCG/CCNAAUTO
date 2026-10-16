import csv
samplefile = open("c:\\github\\general\\devices.csv")
samplereader = csv.reader (samplefile)
for row in samplereader:
    device = row[0]
    location = row[1]
    ip = row[2]
    print (f"{device} is in {location.rstrip()} and its ip is {ip}.")