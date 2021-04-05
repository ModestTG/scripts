#!/usr/bin/env python3

import os
import sys

prefix = sys.argv[1]
path = sys.argv[2]

for i, filename in enumerate(os.listdir(path)):
    dst = f"{prefix}{(i + 1):04}{filename[-4:]}"
    src = f"{path}/{filename}"
    #src = "1920x1080/" + filename
    dst = f"{path}/{dst}"
    #dst = "1920x1080/" + dst
    os.rename(src,dst)
