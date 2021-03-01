from __future__ import print_function, unicode_literals, division


def rgb_to_hex(value):
    rgb_values = value.split(",")
    rgb_values = [int(i) for i in rgb_values]
    print(rgb_values)
    converted_values = []
    for j, value in enumerate(rgb_values):
        converted_values[j] = hex(rgb_values[j])
    print("The converted color value is: #{}{}{}", *converted_values)

print("Convert HTML Colors to and from both RGB and Hex.\nHex format: #000000\nRGB format: ###,###,### (don't need leading zeroes but commas are important)\n")
try:
    color = raw_input("Enter an RGB combination, or Hex value to have it converted. Hex must start with a \'#\': ")
except NameError:
    color = input("Enter an RGB combination, or Hex value to have it converted. Hex must start with a \'#\': ")

if color[0] == '#':
    pass
else:
    rgb_to_hex(color)
