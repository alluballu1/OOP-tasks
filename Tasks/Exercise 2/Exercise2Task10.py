# File name: Exercise2Task10.py
# Author: Alex Porri
# Description: Alarm clock function

# Importing datetime to get the current time

import datetime

# Creating a class for the alarm itself

class alarm_time():

    def __init__(self):
        self.ALARM_HOURS = "00"
        self.ALARM_MINUTES = "00"

    def set_alarm_time(self):
        self.ALARM_HOURS = str(input("Set alarm Hour: "))
        self.ALARM_MINUTES = str(input("Set alarm Minutes: "))

    def get_times(self):
        return self.ALARM_HOURS + self.ALARM_MINUTES

# Current time as hours and minutes, separately. For some reason didn't work without making them global variables

CURRENT_HOUR = datetime.datetime.now().strftime("%H")
CURRENT_MINUTES = datetime.datetime.now().strftime("%M")


def alarm_clock():
    global CURRENT_HOUR
    global CURRENT_MINUTES

    SET_TIME = alarm_time()
    SET_TIME.set_alarm_time()
    ALARM_TIME = SET_TIME.get_times()

    while 1 > 0:

        CURRENT_HOUR = datetime.datetime.now().strftime("%H")
        CURRENT_MINUTES = datetime.datetime.now().strftime("%M")
        if CURRENT_HOUR + CURRENT_MINUTES == ALARM_TIME:
            break
    print("Wake up!")

alarm_clock()
