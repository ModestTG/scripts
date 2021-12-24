#!/usr/bin/env python3
import sys
import json
import requests

with open(sys.argv[2], "r") as f1, open(sys.argv[1], "r") as f2:
    endpoints = json.load(f1)
    folders = json.load(f2)

new_checks = []
for folder in folders:
    check_exists = False
    for check in endpoints["checks"]:
        if folder in check["name"]:
            check_exists = True
            break
    if not check_exists:
        # print(f"check does not exist for {folder}")
        new_checks.append(folder)
# Time in seconds (1 day, 7 days, 31 days)
periods = {"daily": 86400, "weekly": 604800, "monthly": 2678400}
for item in new_checks:
    for period in periods:
        data = {}
