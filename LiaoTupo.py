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

jiejietupo = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\tupo\jiejietupo.png'
jingong = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\tupo\jinggong.png'
victory = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\tupo\victory.png'

tupoConfirm = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\tupo\tupoConfirm.png'
tiaozhanagain = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yysSH\tupo\tiaozhanagain.png'
print(pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9))
tupoPosition = pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9)
# if 攻破0 进4 退4

firstPosition = pyautogui.Point(tupoPosition.x - 350, tupoPosition.y + 120)


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
    time.sleep(1)
    clickposition(position)

    AutoGuiUtil.clickImg(jingong)


def getRes(currentPosition):
    print("准备挑战")
    if AutoGuiUtil.findImg(victory):
        print("success")
        clickposition(tupoPosition)
        return 1
    if AutoGuiUtil.findImg(tiaozhanagain):
        logger.warning("fail")
        return 2
    if AutoGuiUtil.findImg(jiejietupo):
        print("jiejietupo")
        intoTupo(currentPosition)
        return 0
    print("fight")
    time.sleep(3)
    return "fighting"


def jingongs(current, tupo):
    times = 0

    while times < 5:
        res = getRes(current)
        if res != 1:
            if res == 2:
                clickposition(tupo)
                time.sleep(1)
                intoTupo(current)

            times = times + 1
            continue
        return
    print("超过时间")
    while 1:
        print("等待退出")

        res = getRes(current)
        if res == 2:
            return "fail"
        if res != 1:
            continue
        return



def clickposition(position):
    pyautogui.click(position.x + random.randint(-10, 10) / 2
                    , position.y + random.randint(-10, 10) / 2
                    , clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")


if __name__ == '__main__':
    ## todo while没有突破券 退出
    tupoPosition = pyautogui.locateCenterOnScreen(jiejietupo, confidence=0.9)
    # if 攻破0 进4 退4
    tupoPosition = pyautogui.Point(tupoPosition.x, tupoPosition.y + 10)
    firstPosition = pyautogui.Point(tupoPosition.x, tupoPosition.y + 110)
    current = firstPosition
    failTime = 0
    for i in range(100):
        clickposition(pyautogui.Point(tupoPosition.x + 300, tupoPosition.y + 10))
        time.sleep(1)
        print(current)
        if jingongs(current, tupoPosition) == "fail":
            failTime = failTime + 1
            print(current)
            current = pyautogui.Point(firstPosition.x + failTime % 2 * 300,
                                      firstPosition.y + 140 * (int(failTime / 2)))
