#!/usr/bin/env python3

import requests
import json

# API key on file on local machine for security
api_key = ""
base_url = ""
api_prefix = "E:\\Code\\"  # Change this based on git location

with open(api_prefix + "scripts\\python\\tautulli\\api.txt", "r") as f:
	api_key = str.strip(f.read())
	base_url = f"http://esxi.local:8181/api/v2?apikey={api_key}&cmd="


def get_user_cr():
	users = {}
	with open("tautulli_users.json", "r") as f:
		users = json.load(f)
	return users


def get_users_table():
	url = f"{base_url}get_users_table"
	response = requests.get(url)
	return response.json()
