from __future__ import print_function, unicode_literals

output = []
with open("show_vlan.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.split()
    if line[0].isnumeric():
        output.append((line[0], line[1]))

print(output)
