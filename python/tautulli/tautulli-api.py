#!/usr/bin/env python3

import requests
import json

# API key on file on local machine for security
api_key = ""
api_prefix = "/home/docker/code/"  # Change this based on git location

# print("Opening api doc")
with open(api_prefix + "scripts/python/tautulli/api.txt", "r") as f:
	# print("api doc open")
	api_key = str.strip(f.read())

# print("api doc closed")


def get_watched_time(days, userlist):
	"""
	Gets watch data based on user and days specified
	"""
	watch_list = []
	# API data at https://github.com/Tautulli/Tautulli-Wiki/wiki/Tautulli-API-Reference
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_user_watch_time_stats&query_days={days}&user_id="
	for user in userlist:
		# print("request " + str(days) + user + " get")
		response = requests.get(url + str(userlist[user]))
		# print("request " + str(days) + user + " responded")
		response_json = json.loads(response.text)
		watch_list.append({
			"measurement": "Watch_Time_" + str(days) + "_Days",
			"user": user,
			"total_time": response_json["response"]["data"][0]["total_time"],
			"total_plays": response_json["response"]["data"][0]["total_plays"]
		})
	return watch_list


def get_user_list():
	"""
	Gets list of users
	"""
	user_list = {}
	# API data at https://github.com/Tautulli/Tautulli-Wiki/wiki/Tautulli-API-Reference
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_users"
	# print("request user get")
	response = requests.get(url)
	# print("request user respond")
	response_json = json.loads(response.text)
	for i in response_json["response"]["data"]:
		user_list[i["friendly_name"]] = i["user_id"]
	return user_list


def print_data(*watch_lists):
	print_list = []
	for i in watch_lists:
		for j in i:
			print_list.append(j)
	print(json.dumps(print_list))


print_data(get_watched_time(10000, get_user_list()), get_watched_time(7, get_user_list()))
