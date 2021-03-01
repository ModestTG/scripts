from __future__ import print_function, unicode_literals, division
import os

WINDOWS = True

base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_addr = []
for i in range(1,255):
    ip_addr.append("10.0.0." + str(i))

for i, item in enumerate(ip_addr):
    print(str(i) + " ---> " + item)

new_ip_addr = ip_addr[2:6]
for item in new_ip_addr:
    os.system(base_cmd + item)