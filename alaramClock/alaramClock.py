import datetime
import os
import random
import time
import webbrowser


# if video file is not in system then create one


if not os.path.isfile("ss.txt"):
    print("Creating ss.txt")
    with open("alramVideos.txt", 'w') as alarmfile:
        alarmfile.write("https://www.youtube.com/watch?v=YwANQb4phH0")


def checkAlarmInput(alarmtime):
    if len(alarmtime) == 1:  # hour format
        if alarmtime[0] < 24 and alarmtime[0] >= 0:
            return True
    if len(alarmtime) == 2:
        if alarmtime[0] < 24 and alarmtime[0] >= 0 and alarmtime[1] < 60 and alarmtime[1] >= 0:
            return True
    elif len(alarmtime) == 3:
        if alarmtime[0] < 24 and alarmtime[0] >= 0 and alarmtime[1] < 60 and alarmtime[1] >= 0 and alarmtime[2] < 60 and alarmtime[2] > 0:
            return True
    return False


print("Seta a time for the alarm")
while True:
    alarmInput = input(": ")
    try:
        alarmtime = [int(n) for n in alarmInput.split(":")]
        if checkAlarmInput(alarmtime):
            break
        else:
            raise ValueError
    except ValueError:
        print("error in input format of time")

# convert the larm time in hh:mm or h:m:s all to seconds

secondHms = [3600, 60, 1]
alarmseconds = sum(
    [a*b for a, b in zip(secondHms[:len(alarmtime)], alarmtime)])

# get the currwnt time of day in seconds
now = datetime.datetime.now()
currentTimeSeconds = sum(
    [a*b for a, b in zip(secondHms, [now.hour, now.minute, now.second])])

# calculalte the ni of seconds until the alarm goes off
timeDiffSeconds = alarmseconds-currentTimeSeconds
# if time is negative setalaraam for next day
if timeDiffSeconds < 0:
    timeDiffSeconds += 86400

# display the amount of time until the alarm goes off
print("Alarm set to go off in %s" % datetime.timedelta(seconds=timeDiffSeconds))
# sleep until alaram rings
time.sleep(timeDiffSeconds)

# time for alram to go off
print("wake up")
with open("alarmVideos.txt", "r") as alarmfile:
    videos = alarmfile.readlines()

webbrowser.open(random.choice(videos))
