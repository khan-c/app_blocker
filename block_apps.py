#!/usr/bin/env python3
import subprocess
import getpass
import sys
import time
import datetime

applications = ["steam"]
start_date = 0
end_date = 4
start_time = 8
end_time = 18


while True:
    current_time = time.localtime(time.time())
    wday = current_time.tm_wday
    hour = current_time.tm_hour
    print(current_time)

    if (hour >= start_time & hour < end_time & wday >= start_date & wday <= end_date):
        cmd = "ps -u "+getpass.getuser()
        applist = subprocess.check_output(
            ["/bin/zsh", "-c", cmd]).decode("utf-8")
        for application in applications:
            if application in applist:
                action = "pkill "+application
                subprocess.Popen(["/bin/zsh", "-c", action])

    time.sleep(5)
