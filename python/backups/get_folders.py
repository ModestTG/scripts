#!/usr/bin/env python3

from paramiko import SSHClient
import json
import sys

# Should be in the form "user@server:folder_path"
folder_path = sys.argv[1]
user = folder_path.split("@")[0]
server = folder_path.split("@")[1].split(":")[0]
folders = folder_path.split("@")[1].split(":")[1]
folder_name = folder_path.split("@")[1].split(":")[1].split("/")[-1]

client = SSHClient()
client.load_host_keys("/home/eweishaar/.ssh/known_hosts")
client.connect(server, username=user)

stdin, stdout, stderr = client.exec_command(f"ls {folders}")
folders = stdout.read().decode("utf8").split("\n")[:-1]

with open(f"folders_{server}_{folder_name}.json", "w") as f:
    json.dump(folders, f)

stdin.close()
stdout.close()
stderr.close()
client.close()
