from __future__ import print_function, unicode_literals, division

with open('show_ip_int_brief.txt') as f:
    lines = f.readlines()

data = lines[5].split()
data_tuple = (data[0], data[1])
print(data_tuple)
