#!/usr/bin/env python3

import os

for i, filename in enumerate(os.listdir("1920x1080")):
    dst = f"wp_{(i + 1):04}{filename[-4:]}"
    src = "1920x1080/" + filename
    dst = "1920x1080/" + dst
    os.rename(src,dst)
