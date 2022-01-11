#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/monthly && tar czvf /mnt/backup/$i/monthly/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
curl http://docker.lan.ewhomelab.com:8000/ping/f30feea2-632c-4da0-b5ab-c2425b8e5f04
find /mnt/backup/**/monthly/* -mtime + -delete
find /mnt/backup/* -empty -type d -delete
