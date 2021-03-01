from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.lstrip().rstrip()
elements = show_version.split(" ")
model_number = elements[8]
serial_number = elements[15]

print("Cisco Model?")
print("cisco" in model_number.lower())
print("\nModel 881?")
print("881" in model_number)
print(f"\nSerial: {serial_number}\nModel: {model_number}")  # Formatting style only available in Python 3.6 and newer
