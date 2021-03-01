from __future__ import print_function, unicode_literals, division
import re

with open("show_version.txt") as f:
    content = f.read()

os_version = re.search(r'Version (.)+,', content)
sn_version = re.search(r'*0 .+', content)
print(sn_version.group(0))
