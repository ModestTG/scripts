#!/usr/bin/env python3

import tautulli_api
import json


def main():
    measurement = "Tautulli: get_libraries_table"
    libs = tautulli_api.get_libraries_table()
    output_list = []
    tags = [
        "section_name"
    ]
    fields = [
        "count",
        "parent_count",
        "child_count"
    ]
    for i in libs["response"]["data"]["data"]:
        temp_dir = {}
        temp_dir["t_measurement"] = measurement
        tag_vals = [i[x] for x in tags]
        temp_dir.update(dict(zip([f"t_{x}" for x in tags], tag_vals)))
        field_vals = [i[x] for x in fields]
        temp_dir.update(dict(zip([f"f_{x}" for x in fields], field_vals)))
        output_list.append(temp_dir)
    print(json.dumps(output_list))


if __name__ == "__main__":
    main()
