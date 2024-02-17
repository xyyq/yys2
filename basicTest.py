import datetime
import time

import pyautogui

import AutoGuiUtil

now = datetime.datetime.now()
allButton = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\allButton.png'

print(AutoGuiUtil.getPosition(allButton))
time.sleep(5)

print(pyautogui.position())
allButtonPosition = pyautogui.locateCenterOnScreen(allButton, confidence=0.9)
clickPosition = pyautogui.position(allButtonPosition.x + 180, allButtonPosition.y - 100)
AutoGuiUtil.clickposition(clickPosition)