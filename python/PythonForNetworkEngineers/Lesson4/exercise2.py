ip_houston = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.3",
    "10.0.0.1",
    "10.0.0.5",
    "10.0.0.6",
    "10.0.0.7",
    "10.0.0.20",
    "10.0.0.30",
    "10.0.0.5",
    "10.0.0.89"
]

ip_atlanta = [
    "10.0.1.4",
    "10.0.2.4",
    "10.0.3.4",
    "10.0.4.4",
    "10.0.5.4",
    "10.0.6.4",
    "10.0.7.4",
    "10.0.8.4",
    "10.0.9.4",
    "10.0.0.5",
    "10.0.10.4",
    "10.0.11.4",
    "10.0.12.4",
    "10.0.13.4",
    "10.0.14.4",
    "10.0.15.4",
]

ip_chicago = [
    "10.0.0.4",
    "10.0.0.4",
    "10.0.0.4",
    "10.0.0.8",
    "10.0.0.7",
    "10.1.0.4",
]

set_houston = set(ip_houston)
set_atlanta = set(ip_atlanta)
set_chicago = set(ip_chicago)

print(set_houston.intersection(set_atlanta))
print(set_atlanta & set_chicago & set_houston)
print(set_chicago | set_houston)
