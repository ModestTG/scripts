#!/usr/bin/env python3

import praw
import os
import re
import urllib.request
from tqdm import tqdm, trange

secret = ""
client_id = ""

wp_dir_prefix = "/home/eweishaar/wallpapers"
k1_dir = wp_dir_prefix + "/1920x1080"
k2_dir = wp_dir_prefix + "/2560x1440"
k4_dir = wp_dir_prefix + "/3840x2160"

dir_list = [k1_dir, k2_dir, k4_dir]

with open("secret", "r") as f:
    client_id = f.readline().strip()
    secret = f.readline().strip()

print("Getting Existing Directory Count")
dir_count = {}
for i in dir_list:
    dir_count[i.lstrip(wp_dir_prefix)] = len(os.listdir(i))

reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        user_agent="python:reddit-wp-crawler:v1.0.0 (by u/ModestTG)"
)

print("Getting Subreddit Info")
sub_limit = 10
subreddit = reddit.subreddit("wallpaper").hot(limit=sub_limit)

pics = []
print("Compiling Info")
for submission in subreddit:
    pics.append((submission.title, submission.url))


#print(pics)
#bar = tqdm(desc="Downloading Images", total=sub_limit)
for pic in pics:
    #print(pic)
    if re.search(r'1920', pic[0]):
        urllib.request.urlretrieve(pic[1], f'{k1_dir}/wp_{dir_count["1920x1080"] + 1:04}.{pic[1][-3:]}')
        dir_count["1920x1080"] += 1
        continue
    elif re.search(r'2560', pic[0]):
        #print("2560")
        continue
    elif re.search(r'3840', pic[0]):
        #print("3840")
        continue
    else:
        continue
        #print("irregular size")


