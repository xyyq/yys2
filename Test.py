import time
import random
import pyautogui


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


time.sleep(2)


print(pyautogui.position())

## 第28 Point(x=922, y=535)

## 取消探索 Point(x=837, y=274)

## 探索 Point(x=769, y=586)

## 退出 Point(x=44, y=108)

## confirm Point(x=607, y=468)



#
# pyautogui.click(x=922, y=535,clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
#                         duration=0.3 + random.randint(-10, 10) / 100, button="left")

img = "/Users/sifatasinant/Downloads/in_dungeon.PNG"
x, y = pyautogui.position()
pyautogui.dragTo(x + 300, y, duration= 0.2, button='left')
#clickimg(img)

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
