#!/usr/bin/env python3

import os
import sys
import random
import string
from tqdm import tqdm

# File prefix
prefix = sys.argv[1]

# File path
path = sys.argv[2]


def main():
    if os.name == "posix":
        rename_posix(prefix, path)


def rename_posix(prefix, path):
    random_names_list = sorted(
        [
            "".join(random.choices(string.ascii_letters + string.digits, k=16))
            for i in range(len(os.listdir(path)))
        ]
    )
    # print("First Loop")
    for i, filename in enumerate(sorted(os.listdir(path))):
        dst = f"{random_names_list[i]}{(i + 1):04}{filename[-4:]}"
        src = f"{path}/{filename}"
        dst = f"{path}/{dst}"
        try:
            os.rename(src, dst)
            # print(f"renaming {src} to {dst}")
        except FileExistsError:
            print("Duplicate Files")
            break

    # print("Second Loop")
    for i, filename in enumerate(tqdm(sorted(os.listdir(path)))):
        dst = f"{prefix}{(i + 1):04}{filename[-4:]}"
        src = f"{path}/{filename}"
        dst = f"{path}/{dst}"
        try:
            os.rename(src, dst)
            # print(f"renaming {src} to {dst}")
        except FileExistsError:
            print("Duplicate Files")
            break


if __name__ == "__main__":
    main()
