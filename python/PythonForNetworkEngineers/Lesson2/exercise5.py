from __future__ import print_function, unicode_literals, division

with open('show_ip_bgp_summ.txt') as f:
    lines = f.readlines()

first_line = lines[0].split()
last_line = lines[-1].split()
print(first_line[-1], last_line[0])
