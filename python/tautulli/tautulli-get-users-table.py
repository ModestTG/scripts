import tautulli_api
import json


def main():
    measurement = "Tautulli: get_users_table"
    users = tautulli_api.get_user_cr()
    output_list = []
    rem_list = ["row_id",
                "user_thumb",
                "history_row_id",
                "ip_address",
                "platform",
                "player",
                "rating_key",
                "media_type",
                "thumb",
                "parent_title",
                "year",
                "media_index",
                "parent_media_index",
                "live",
                "originally_available_at",
                "guid",
                "transcode_decision",
                "do_notify",
                "keep_history",
                "allow_guest",
                "is_active"]
    data = tautulli_api.get_users_table()
    for i in data["response"]["data"]["data"]:
        [i.pop(key) for key in rem_list]
        for j in users.items():
            if j[0] == i["username"]:
                i["friendly_name"] = j[1]
                break
        i["measurement"] = measurement
        output_list.append(i)
    print(json.dumps(output_list))


if __name__ == "__main__":
    main()
