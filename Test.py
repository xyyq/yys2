import time
import random
import pyautogui

import AutoGuiUtil

allButton = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\allButton.png'


injiejieButton = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\injiejieButton.png'

AutoGuiUtil.clickImg(allButton)

def clickimg(img):
    try:

        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        pyautogui.click(location.x / 2, location.y / 2, clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        print("单击左键", img)
        time.sleep(0.5)
        return True

    except Exception as e:
        print("未找到图片", img)
        print(e)
        return False


time.sleep(3)

## 第28 Point(x=922, y=535)

## 取消探索 Point(x=837, y=274)

## 探索 Point(x=769, y=586)

## 退出 Point(x=44, y=108)

## tupoConfirm Point(x=607, y=468)

##haoyou  Point(x=454, y=227)
##1Point(x=636, y=344)
# 2Point(x=655, y=466)


#
# pyautogui.click(x=922, y=535,clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
#                         duration=0.3 + random.randint(-10, 10) / 100, button="left")

##
##haoyou = r'resource/douyu6.png'
##x, y = pyautogui.locateCenterOnScreen(haoyou, confidence=0.8)
##print("x{},y{}".format(x, y))

##
##
time.sleep(2)

pyautogui.press("esc")
print("11")
time.sleep(2)
pyautogui.press("esc")
print("22")

print(pyautogui.position())

xhaoyou, yhaoyou = pyautogui.locateCenterOnScreen(haoyou, confidence=0.8)
for i in range(4):
    pyautogui.click(xhaoyou + 200, yhaoyou + 120 * (i + 1), clicks=1, interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")

# clickimg(img)

#
# try:
#     x, y = pyautogui.locateCenterOnScreen(img, confidence=0.6)
#     print("x {}, y{}".format(x / 2, y / 2))
#     x = x / 2 + 110
#     y = y / 2 - 30
#     print("x {}, y{}".format(x, y))
#
#     # 先左键点击挑战
#     pyautogui.click(x, y, clicks=2,
#                     interval=0.4 + random.randint(-10, 10) / 100,
#                     duration=0.3 + random.randint(-10, 10) / 100, button="left")
#     print("单击左键", img)
#     time.sleep(0.5)
#
# except Exception as e:
#     print("未找到移动图片")
#     print(e)
#
