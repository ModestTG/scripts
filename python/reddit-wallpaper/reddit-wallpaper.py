#!/usr/bin/env python3

import praw
import os
import re
import urllib.request
from tqdm import tqdm

sub = "wallpaper"
sub_limit = 1000
prefix = "/home/eweishaar/wallpapers"

def main():
    wp_dir_prefix = prefix
    k1_dir = wp_dir_prefix + "/1920x1080"
    k2_dir = wp_dir_prefix + "/2560x1440"
    k4_dir = wp_dir_prefix + "/3840x2160"
    dir_list = [k1_dir, k2_dir, k4_dir]
    
    dir_count = {}
    for i in dir_list:
        dir_count[i.lstrip(prefix)] = len(os.listdir(i))

    secret = ""
    client_id = ""
    with open("secret", "r") as f:
        client_id = f.readline().strip()
        secret = f.readline().strip()

    reddit = praw.Reddit(
            client_id=client_id,
            client_secret=secret,
            user_agent="python:reddit-wp-crawler:v1.0.0 (by u/ModestTG)"
    )
    subreddit = reddit.subreddit(sub).top("all", limit=sub_limit)

    pics = []
    for submission in subreddit:
        pics.append((submission.title, submission.url))

    bar = tqdm(desc="Downloading Images", total=sub_limit)
    for pic in pics:
        if re.search(r'1920', pic[0]):
            try:
                urllib.request.urlretrieve(pic[1], f'{k1_dir}/wp_{dir_count["1920x1080"] + 1:04}.{pic[1][-3:]}')
                dir_count["1920x1080"] += 1
                bar.update()
                continue
            except urllib.error.HTTPError as e:
                print(e)
                bar.update()
                continue
        elif re.search(r'2560', pic[0]):
            try:
                urllib.request.urlretrieve(pic[1], f'{k2_dir}/wp_{dir_count["2560x1440"] + 1:04}.{pic[1][-3:]}')
                dir_count["2560x1440"] += 1
                bar.update()
                continue
            except urllib.error.HTTPError as e:
                print(e)
                bar.update()
                continue
        elif re.search(r'3840', pic[0]):
            try:
                urllib.request.urlretrieve(pic[1], f'{k4_dir}/wp_{dir_count["3840x2160"] + 1:04}.{pic[1][-3:]}')
                dir_count["3840x2160"] += 1
                bar.update()
                continue
            except urllib.error.HTTPError as e:
                print(e)
                bar.update()
                continue

    print(f'{dir_count["1920x1080"]} 1k wallpapers downloaded')
    print(f'{dir_count["2560x1440"]} 2k wallpapers downloaded')
    print(f'{dir_count["3840x2160"]} 4k wallpapers downloaded')


if __name__ == "__main__":
    main()
