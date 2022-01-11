#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/daily && tar czvf /mnt/backup/$i/daily/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
curl http://docker.lan.ewhomelab.com:8000/ping/d804be87-279d-439a-98f6-8ac7f2b8b6d7
find /mnt/backup/**/daily/* -mtime +7 -delete
find /mnt/backup/* -empty -type d -delete
