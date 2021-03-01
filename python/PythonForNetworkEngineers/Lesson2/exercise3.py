from __future__ import print_function, unicode_literals, division
from pprint import pprint
with open('show_arp.txt') as f:
    lines = f.readlines()

lines = lines[1:]
pprint(lines)
lines.sort()
new_list = lines[0:3]
new_string = "\n".join(new_list)
with open("arp_entires.txt", "w") as f:
    f.write(new_string)
