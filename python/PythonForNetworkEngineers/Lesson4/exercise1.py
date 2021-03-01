from __future__ import print_function, unicode_literals, division

dict1 = {
    'ip_addr': '10.0.0.1',
    'vendor': 'OSI',
    'username': 'admin',
    'password': 'admin'
}
bgp_fields = {
    "bgp_as": "",
    "peer_as": "",
    "peer_ip": ""
}
print(dict1['ip_addr'])
if dict1['vendor'] == 'cisco':
    dict1['platform'] = 'ios'
elif dict1['vendor'] == 'juniper':
    dict1['platform'] = 'junos'
dict1.update(bgp_fields)

for key in dict1:
    print(key)

for key, value in dict1.items():
    print(key, value)
