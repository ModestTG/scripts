# WIP

from __future__ import print_function, unicode_literals
import subprocess
import os
import json

directory_mkv = r"F:\temp2"
directory_json = r"F:\temp2\json"
track_list = []
track_list2 = []
track_list3 = []
filenames_mkv = os.listdir(directory_mkv)
filenames_mkv.sort()
for filename in filenames_mkv:
    if ".mkv" in filename:
        with open(directory_json + "\\" + filename + ".json", "w") as f:
            f.write(subprocess.getoutput("mkvmerge -i -F json " + filename))

json_filenames = os.listdir(directory_json)
json_filenames.sort()

# print(filenames_mkv)
# print(json_filenames)
for item in json_filenames:
    with open(directory_json + "\\" + item) as f:
        file_data = json.load(f)
        for data in file_data["tracks"]:
            if "AAC" in data["codec"] and data["properties"]["language"] == "eng":
                track_list.append(data["id"])

print(track_list)
print(len(track_list))
