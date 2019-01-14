import sys
import time
import pyttsx
from tkinter import *

engine = pyttsx.init()



master = Tk()

time_start = time.time()
seconds = 0
minutes = 0

while True:
        try:
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            print ("\{minutes} Minutes {seconds} Seconds".format(minutes = minutes, seconds = seconds))
            #w = Label(master, text='"\{minutes} Minutes {seconds} Seconds".format(minutes = minutes, seconds = seconds')
            if seconds >= 60:
                minutes += 1
                seconds = 0
            if minutes == 25:
                engine.say("HEY! Time is up")
                engine.runAndWait()

        except KeyboardInterrupt as e:
            break
