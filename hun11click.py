import random
import time

import pyautogui

while 1:
    pyautogui.click(pyautogui.position().x, pyautogui.position().y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
    time.sleep(3)