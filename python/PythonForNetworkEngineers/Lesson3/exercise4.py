from __future__ import print_function, unicode_literals, division

arp_table = [('10.220.88.1', '0062.ec29.70fe'),
             ('10.220.88.20', 'c89c.1dea.0eb6'),
             ('10.220.88.21', '1c6a.7aaf.576c'),
             ('10.220.88.28', '5254.aba8.9aea'),
             ('10.220.88.29', '5254.abbe.5b7b'),
             ('10.220.88.30', '5254.ab71.e119'),
             ('10.220.88.32', '5254.abc7.26aa'),
             ('10.220.88.33', '5254.ab3a.8d26'),
             ('10.220.88.35', '5254.abfb.af12'),
             ('10.220.88.37', '0001.00ff.0001'),
             ('10.220.88.38', '0002.00ff.0001'),
             ('10.220.88.39', '6464.9be8.08c8'),
             ('10.220.88.40', '001c.c4bf.826a'),
             ('10.220.88.41', '001b.7873.5634')]

i = 0
while i < len(arp_table):
    output = ""
    mac_parts = arp_table[i][1].split(".")
    for element in mac_parts:
        output += element[0:2].upper() + "." + element[2:4].upper() + "."
    print(output[:-1])
    i += 1