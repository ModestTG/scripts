#!/usr/bin/env python3

from paramiko import SSHClient
import json

client = SSHClient()
client.load_host_keys('/home/eweishaar/.ssh/known_hosts')

client.connect('docker.lan.ewhomelab.com', username="docker")
stdin, stdout, stderr = client.exec_command('ls /home/docker/container_data')

folders = stdout.read().decode("utf8").split("\n")[:-1]
print(type(folders))
print(folders)

with open('folders.json', "w") as f:
    json.dump(folders, f)

stdin.close()
stdout.close()
stderr.close()
client.close()
