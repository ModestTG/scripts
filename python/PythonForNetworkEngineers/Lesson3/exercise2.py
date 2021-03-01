from __future__ import print_function, unicode_literals, division

default_gateway, arista3 = False, False
with open("show_arp.txt") as f:
    lines = f.readlines()
del lines[0]
for line in lines:
    line = line.split()
    ip_addr = line[1]
    mac_addr = line[3]
    if "10.220.88.1" in ip_addr:
        print("Default gateway IP/MAC: " + ip_addr + "/" + mac_addr)
        default_gateway = True
    elif "10.220.88.30" in ip_addr:
        print("Arista 3 gateway IP/MAC: " + ip_addr + "/" + mac_addr)
        arista3 = True
    elif default_gateway and arista3:
        break
