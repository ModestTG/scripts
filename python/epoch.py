from __future__ import print_function, unicode_literals
import time


try:
    date_time = raw_input("Input your Date (MM/DD/YYYY hh:mm:ss): ")
except NameError:
    date_time = input("Input your Date (MM/DD/YYYY hh:mm:ss): ")

date_time_dmy = tuple(map(int, date_time.split(" ")[0].split("/")))
date_time_hms = tuple(map(int, date_time.split(" ")[1].split(":")))

time_tuple = (date_time_dmy[2], date_time_dmy[1], date_time_dmy[0], date_time_hms[0], date_time_hms[1],
              date_time_hms[2], 0, 0, -1)
epochTime = time.mktime(time_tuple)
print(int(epochTime))
