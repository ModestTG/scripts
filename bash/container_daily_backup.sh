#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/daily && tar czf /mnt/backup/$i/daily/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
find /mnt/backup/**/daily/* -mtime +6 -delete
find /mnt/backup/* -empty -type d -delete
