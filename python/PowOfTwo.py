from __future__ import print_function

try:
	exponent = raw_input("Enter an exponent: ")
except NameError:
	exponent = input("Enter an exponent: ")

print('{0:2} {1:<20} {2:<19}'.format("Pow", "Dec", "Hex"))
print("-" * 41)
for i in range(0, int(exponent) + 1):
	print('{0:<3} {1:<20} {2:<19}'.format(i, 2 ** i, hex(2 ** i)))
