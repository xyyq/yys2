import time
import random
import pyautogui
import logging
tupoConfirm = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\tupoConfirm.png'

def clickImg(img):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
        # 先左键点击挑战
        pyautogui.click(location.x, location.y, clicks=1, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        print("单击左键", img)
        time.sleep(0.5)
        return True

    except Exception as e:
        print("未找到图片", img)
        print(e)
        return False


def findImg(img):
    try:
        pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        print("找到图片", img)

        return True
    except Exception as e:
        print("未找到图片", img)
        print(e)
        return False


def inJiyang():
    if findImg(jiyang):
        return

    while not findImg(injiejieButton):
        time.sleep(1)
    clickImg(injiejieButton)
    pass


if __name__ == '__main__':
    findImg(tupoConfirm)
