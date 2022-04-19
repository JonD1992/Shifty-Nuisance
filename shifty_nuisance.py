import keyboard
import time
import random 
from random import randint
import datetime

Nuisance = True

while True:
    if datetime.datetime.now().time().strftime("%H:%M")  == "14:20":
        Nuisance = True

        while Nuisance:
            nuisance_time = randint(0,1)
            time.sleep(nuisance_time)
            print('nuisance time ongoing')
            keyboard.press('shift')
            shifty_time = randint(0,1)
            time.sleep(shifty_time)
            keyboard.release('shift')
           

    if datetime.datetime.now().time().strftime("%H:%M:%S")  == "14:24:20":

        Nuisance = False

