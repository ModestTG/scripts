from __future__ import print_function, unicode_literals

ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'

octets = ip_addr1.split(".")

print("\n")
print("-" * 80)
# print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3))
# print("{:10}{:10}{:10}{:10}".format(*octets))
# print("%s %s" % (ip_addr1, ip_addr2))
print(f"{ip_addr1:20}")  # Only available in Python 3.6.x and higher
print("-" * 80)
print("\n")
