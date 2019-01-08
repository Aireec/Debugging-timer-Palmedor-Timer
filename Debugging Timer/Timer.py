import sys
import time
import pyttsx

engine = pyttsx.init()

time_start = time.time()
seconds = 0
minutes = 0

while True:
    try:
        sys.stdout.write("\{minutes} Minutes {seconds} Seconds".format(minutes = minutes, seconds = seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
        if minutes == 25:
            engine.say("HEY! Time is up")
            engine.runAndWait()
    except KeyboardInterrupt as e:
        break