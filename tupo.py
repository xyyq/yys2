import random
import string

import pyautogui
import time
import xlrd
import pyperclip

import logging

import AutoGuiUtil
import jiyang
import logging.config

# 加载配置
logging.config.fileConfig(r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\config\logging.conf')

# 创建 logger
logger = logging.getLogger()
#
# Point(x=743, y=410)
# Point(x=393, y=542)
# Point(x=764, y=535)
# Point(x=375, y=693)


time.sleep(3)

jiejietupo = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\jiejietupo.png'
jingong = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\jingong.png'
victory = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\victory.png'

tupoConfirm = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\tupoConfirm.png'
tiaozhanagain = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\tiaozhanagain.png'
print(pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9))
position = pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9)
# if 攻破0 进4 退4

firstPosition = pyautogui.Point(position.x - 350, position.y + 140)


def exit2topo():
    print("退出突破")
    time.sleep(2)
    pyautogui.press("esc")
    time.sleep(2)

    AutoGuiUtil.clickImg(tupoConfirm)
    time.sleep(2)
    pyautogui.click(firstPosition.x, firstPosition.y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")


def intoTupo(position):
    print("点击突破挑战")
    time.sleep(2)
    pyautogui.click(position.x, position.y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")

    AutoGuiUtil.clickImg(jingong)


def shuaxing(firstPosition):
    for i in range(4):
        if not AutoGuiUtil.findImg(jiejietupo):
            clickposition(position)
        intoTupo(firstPosition)
        time.sleep(2)
        exit2topo()
        time.sleep(3)


def getRes(currentPosition):
    print("准备挑战")
    if AutoGuiUtil.findImg(victory):
        print("success")
        clickposition(position)
        return 1
    if AutoGuiUtil.findImg(tiaozhanagain):
        logger.warning("fail")

        clickposition(position)
        intoTupo(currentPosition)
        return 0
    if AutoGuiUtil.findImg(jiejietupo):
        print("jiejietupo")

        intoTupo(currentPosition)
        return 0
    print("fight")
    time.sleep(15)
    return 0


def jingongs(firstPosition):
    for x in range(3):
        for y in range(3):
            time.sleep(2)
            clickposition(position)
            time.sleep(1)
            print("第 %s行，第 %s列" % (x + 1, y + 1))
            times = 0
            currentPosition = pyautogui.position(firstPosition.x + x * 350, firstPosition.y + y * 140)
            while getRes(currentPosition) == 0 & times < 30:
                print("等待挑战成功")
                times = times + 1
            if times >= 30:
                return "fail"

def clickposition(position):
    pyautogui.click(position.x, position.y, clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")


if __name__ == '__main__':
    ## todo while没有突破券 退出
    position = pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9)
    # if 攻破0 进4 退4

    firstPosition = pyautogui.Point(position.x - 350, position.y + 140)
    for i in range(3):
        time.sleep(6)
        clickposition(position)
        time.sleep(3)

        shuaxing(firstPosition)
        if jingongs(firstPosition) == "fail":
            print("打不过， 算了")
