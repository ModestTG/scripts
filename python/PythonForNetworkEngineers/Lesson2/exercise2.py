from __future__ import print_function, unicode_literals, division

ip_addr = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5']
ip_addr.append('10.0.0.6')
ip_addr.extend(['10.0.0.7', '10.0.0.8'])
ip_addr += ['10.0.0.9', '10.0.0.10']
print(ip_addr)
print(ip_addr[0])
print(ip_addr[-1])
ip_addr.pop(0)
ip_addr.pop()
ip_addr[0] = '2.2.2.2'
print(ip_addr[0])
