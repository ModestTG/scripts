from __future__ import print_function, unicode_literals, division

new_file = open("show_version.txt")
text = new_file.read()
print(text)
print(type(text))
new_file.close()

with open("show_version.txt") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))
