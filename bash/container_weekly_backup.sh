#!/bin/bash

for i in $(ls /home/docker/container_data); do mkdir -p /mnt/backup/$i/weekly && tar czf /mnt/backup/$i/weekly/$i-$(date "+%Y%m%d").tar.gz /home/docker/container_data/$i; done
find /mnt/backup/**/weekly/* -mtime +27 -delete
find /mnt/backup/* -empty -type d -delete
