import random
import string
from threading import Thread

import pyautogui
import time
import xlrd
import pyperclip
import logging
import logging.config

import LogUtil


def clickImg(img):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        pyautogui.click(location.x, location.y, clicks=1, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        LogUtil.logger.info("单击左键 %s" % img)
        time.sleep(0.5)
        return True

    except Exception as e:
        LogUtil.logger.warning("点击未找到图片 %s" % img)
        return False


def clickpositions(position):
    pyautogui.click(position.x, position.y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
def clickCurrent():
    pyautogui.click(pyautogui.position().x, pyautogui.position().y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")

def getPosition(img):
    return pyautogui.locateCenterOnScreen(img, confidence=0.9)


def findImg(img):
    try:
        pyautogui.locateCenterOnScreen(img, confidence=0.9)
        LogUtil.logger.info("找到图片 %s" % img)
        # 先左键点击挑战
        return True
    except Exception as e:
        LogUtil.logger.info("未找到图片 %s" % img)
        return False
