#!/usr/bin/env python3
import json


def api(project, oper):
    if oper not in "ro" and oper not in "w":
        raise ValueError("Incorrect API type (must be 'ro' or 'w')")
    with open("secrets.json", "r") as f:
        secrets = json.load(f)

    for item in secrets:
        if item["project"] == project:
            if oper == "ro":
                return item["api"]["readonly"]
            elif oper == "w":
                return item["api"]["write"]
