#!/usr/bin/env python3
import sys
import requests
import json
import get_api

# ./get_checks.py <HCProjectName>
api_ro = get_api.api(sys.argv[1], "ro")

with open(f'hc_endpoints_{sys.argv[1].replace(" ", "_").lower()}.json', "w") as f:
    headers = {"X-Api-Key": api_ro}
    json.dump(
        requests.get(
            "http://docker.lan.ewhomelab.com:8000/api/v1/checks/", headers=headers
        ).json(),
        f,
    )
