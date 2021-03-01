from __future__ import print_function, unicode_literals, division

port_id, system_name = False, False
with open("show_lldp_neighbors_detail.txt") as f:
    lines = f.readlines()


for line in lines:
    line = line.split(":")
    if "Port id" in line[0]:
        print(line[1])
        port_id = True
    elif "System Name"in line[0]:
        print(line[1])
        system_name = True
    elif port_id and system_name:
        break
