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



mumuFlag = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\jiyang\mumuFlag.png'

def clickImg(img):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        pyautogui.click(location.x + random.randint(-10, 10) / 2,
                        location.y + random.randint(-10, 10) / 2, clicks=1, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        LogUtil.logger.info("单击左键 %s" % img)
        time.sleep(0.5)
        return True

    except Exception as e:
        LogUtil.logger.warning("点击未找到图片 %s" % img)
        return False
def clickImgNolog(img):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        pyautogui.click(location.x + random.randint(-10, 10) / 2,
                        location.y + random.randint(-10, 10) / 2 , clicks=1, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        time.sleep(0.5)
        return True

    except Exception as e:
        return False


def clickpositions(position):
    pyautogui.click(position.x + random.randint(-10, 10) / 2, position.y + random.randint(-10, 10) / 2, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
def clickCurrent():
    pyautogui.click(pyautogui.position().x+ random.randint(-10, 10) / 2, pyautogui.position().y+ random.randint(-10, 10) / 2, clicks=1,
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

def clickCenter():
    point = getPosition(mumuFlag)
    point = pyautogui.Point(point.x + 480, point.y + 388)
    clickpositions(point)
