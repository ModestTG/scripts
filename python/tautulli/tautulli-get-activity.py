#!/usr/bin/env python3

import tautulli_api
import json
import hashlib


def main():
    measurement = "Tautulli: get_activity"
    activity = tautulli_api.get_activity()
    users = tautulli_api.get_user_cr()
    output_list = []
    fields = [
        "stream_count",
        "stream_count_direct_play",
        "stream_count_direct_stream",
        "stream_count_transcode",
        "total_bandwidth",
        "lan_bandwidth",
        "wan_bandwidth"
    ]
    tags = [
        "username",
        "full_title",
        "friendly_name",
        "title",
        "media_type",
        "parent_title",
        "grandparent_title",
        "stream_video_full_resolution",
        "video_decision",
        "quality_profile",
        "platform",
        "location"
    ]
    if int(activity["response"]["data"]["stream_count"]) == 0:
        temp_dir = {}
        zero_vals = [0 for x in fields]
        empty_str = ["" for x in tags]
        temp_dir.update(dict(zip(fields, zero_vals)))
        temp_dir.update(dict(zip(tags, empty_str)))
        output_list.append(temp_dir)
        print(json.dumps(output_list))
    else:
        for i in activity["response"]["data"]["sessions"]:
            temp_dir = {}
            val_global = [activity["response"]["data"][x] for x in fields]
            temp_dir.update(dict(zip([f"f_{x}" for x in fields], val_global)))
            val_session = [i[x] for x in tags]
            temp_dir.update(dict(zip([f"t_{x}" for x in tags], val_session)))
            temp_dir["t_measurement"] = measurement
            temp_dir["fs_hash"] = hashlib.md5(f'{i["session_id"]}{i["session_key"]}{i["username"]}{i["full_title"]}'.encode("utf-8")).hexdigest()
            temp_dir["f_stream_count"] = int(temp_dir["f_stream_count"])
            # print(temp_dir)
            for j in users.items():
                if j[0] == i["username"]:
                    temp_dir["t_friendly_name"] = j[1]
                    break
            output_list.append(temp_dir)
        print(json.dumps(output_list))


if __name__ == "__main__":
    main()
