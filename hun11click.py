import datetime
import random
import time

import pyautogui
import  pydirectinput


while 1:
    pydirectinput.click(pyautogui.position().x, pyautogui.position().y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
    print("click")
    time.sleep(3)