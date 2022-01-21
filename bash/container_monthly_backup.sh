#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/monthly && tar czf /mnt/backup/$i/monthly/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
find /mnt/backup/**/monthly/* -mtime +31 -delete
find /mnt/backup/* -empty -type d -delete
