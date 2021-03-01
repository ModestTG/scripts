# allows print() funtion and bytestrings to work in python2
from __future__ import print_function, unicode_literals

my_str = 'whatever'

ip_addr1 = '8.8.8.8'
print(ip_addr1)
try:
    ip_addr2 = raw_input("Enter an IP Address: ")  # python2 input function
except NameError:
    ip_addr2 = input("Enter an IP Address: ")  # python3 input funtion
print(ip_addr2)
