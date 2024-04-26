import datetime
import random
import time

import pyautogui
import  pydirectinput
time.sleep(2)

x, y = pyautogui.position()
while 1:
    pydirectinput.click( x+ random.randint(-50, 50) ,
                         y + random.randint(-50, 50) ,
                        clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
    print("click")
    time.sleep(random.randint(50, 100) * 0.03)