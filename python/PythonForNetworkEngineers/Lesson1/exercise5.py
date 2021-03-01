from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.split(" ")
mac2 = mac2.split(" ")
mac3 = mac3.split(" ")

mac1_ip_addr = mac1[2]
mac2_ip_addr = mac2[2]
mac3_ip_addr = mac3[2]

mac1_mac_addr = mac1[16]
mac2_mac_addr = mac2[17]
mac3_mac_addr = mac3[15]

print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-" * 20, "-" * 20))
print("{:>20} {:>20}".format(mac1_ip_addr, mac1_mac_addr))
print("{:>20} {:>20}".format(mac2_ip_addr, mac2_mac_addr))
print("{:>20} {:>20}".format(mac2_ip_addr, mac3_mac_addr))
