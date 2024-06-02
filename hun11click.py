import random
import time

import pyautogui

time.sleep(3)
x, y = pyautogui.position()
print(2222)
time.sleep(3)
x1, y1 = pyautogui.position()

while 1:
    pyautogui.click(x + random.randint(-2, 2)
                    ,y + random.randint(-2, 2), clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")

    time.sleep(random.randint(15,25) / 10)
    pyautogui.click(x1 + random.randint(-2, 2)
                    ,y1 + random.randint(-2, 2), clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
    time.sleep(random.randint(15,25) / 10)
