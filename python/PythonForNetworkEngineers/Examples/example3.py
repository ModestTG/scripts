from __future__ import print_function, unicode_literals, division

# This is considered the proper way to open a file, as you do not need to include the f.close() syntax in this block
# This will also flush() a file if you are writing data to a file.
# The 'r' prepending the file path makes this a "raw" string. This string ignores all escape characters ('\')
with open(r"D:\Code\Corporea\txt\declarationofindependance.txt") as f:
    output = f.read()

print(output)
