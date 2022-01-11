#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/weekly && tar czvf /mnt/backup/$i/weekly/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
curl http://docker.lan.ewhomelab.com:8000/ping/7b794127-044d-4efb-aff1-a168cdc61e76
find /mnt/backup/**/weekly/* -mtime +28 -delete
find /mnt/backup/* -empty -type d -delete
