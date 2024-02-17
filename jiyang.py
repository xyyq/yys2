import random
import string
from threading import Thread

import pyautogui
import time

import AutoGuiUtil
import LogUtil

gouyu59 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\gouyu59.png'
gouyu76 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\gouyu76.png'
gouyu67 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\gouyu67.png'
gouyu50 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\gouyu50.png'
douyu6 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\douyu6.png'
douyu5 = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\douyu5.png'

jiyang = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\jiyang.png'
in_jiejie = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\in_jiejie.png'
haoyou = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\haoyou.png'
confirm = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\confirm.png'
jiejieFlag = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\jiejieFlag.png'
injiejieButton = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\injiejieButton.png'
reject = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\reject.png'
allButton = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\allButton.png'
noResource = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\noResource.png'
exitGame = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\exitGame.png'
cancelExit = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\cancelExit.png'
inJiyangJiejie = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\inJiyangJiejie.png'

time.sleep(3)

global jiyangSuccess
jiyangSuccess = False


## x + 200 y + 120

def exitCurent():
    pyautogui.press("esc")
    LogUtil.logger.info("寄养被占用")
    time.sleep(3)
    pyautogui.press("esc")
    time.sleep(3)
    inJiyang()
    AutoGuiUtil.AutoGuiUtil.clickImg(jiyang)

    pass


def back2Top():
    for k in range(10):
        pyautogui.scroll(-1)


def findResource(cardItem):
    try:

        LogUtil.logger.info("准备开始")
        time.sleep(5)
        find = False
        xhaoyou, yhaoyou = pyautogui.locateCenterOnScreen(haoyou, confidence=0.85)

        for i in range(8):
            if find:
                break
            for j in range(4):
                pyautogui.click(xhaoyou + 200, yhaoyou + 120 * (j + 1), clicks=1,
                                interval=0.4 + random.randint(-10, 10) / 100,
                                duration=0.3 + random.randint(-10, 10) / 100, button="left")

                if AutoGuiUtil.findImg(cardItem):
                    AutoGuiUtil.clickImg(in_jiejie)
                    find = True
                    break
                if AutoGuiUtil.findImg(noResource):
                    back2Top()
                    LogUtil.logger.info("发现未放置")
                    return False
                time.sleep(3)
            if find:
                break
            back2Top()

        time.sleep(3)
        if not find:
            LogUtil.logger.info("未找到 %s" % cardItem)
            return False
        ##todo 根据图片定位来
        if AutoGuiUtil.findImg(allButton):
            allButtonPosition = pyautogui.locateCenterOnScreen(allButton, confidence=0.9)
            clickPosition = pyautogui.position(allButtonPosition.x + 180, allButtonPosition.y - 100)
            AutoGuiUtil.clickpositions(clickPosition)
            LogUtil.logger.info("开始寄养")
            if AutoGuiUtil.findImg(confirm):
                LogUtil.logger.info("点击寄养")
                if AutoGuiUtil.clickImg(confirm):
                    return True
        ##exit
        LogUtil.logger.info("寄养失败")
        time.sleep(10)

        exitCurent()
        findResource(cardItem)

        return True
        pass
    except Exception as e:
        LogUtil.logger.error("findResource error %s" % e)
        return False
def inJiyang():
    try:
        if AutoGuiUtil.findImg(jiyang):
            return

        while not AutoGuiUtil.findImg(jiejieFlag):
            exit2jiejie()
            time.sleep(3)
        AutoGuiUtil.clickImg(injiejieButton)
        pass
    except Exception as e:
        LogUtil.logger.error("inJiyang error %s" % e)


def exit2jiejie():
    try:

        if AutoGuiUtil.findImg(exitGame):
            AutoGuiUtil.clickImg(cancelExit)
            time.sleep(3)
            exit2jiejie()

        if AutoGuiUtil.findImg(inJiyangJiejie):
            AutoGuiUtil.clickImg(inJiyangJiejie)
            time.sleep(3)
            exit2jiejie()

        if not AutoGuiUtil.findImg(jiejieFlag):
            pyautogui.press("esc")
            time.sleep(5)
            exit2jiejie()
        pass
    except Exception as e:
        LogUtil.logger.error("exit2jiejie error %s" % e)



def waitJiyang():
    try:

        inJiyang()
        LogUtil.logger.info("进入 寄养")
        time.sleep(30)

        if not AutoGuiUtil.findImg(jiyang):
            time.sleep(30)
            exit2jiejie()
            waitJiyang()
        pass
    except Exception as e:
        LogUtil.logger.error("waitJiyang error %s" % e)


def startJiyang():
    try:
        waitJiyang()
        inJiyang()
        if AutoGuiUtil.findImg(jiyang):
            AutoGuiUtil.clickImg(jiyang)
            LogUtil.logger.info("进入好友寄养列表")
            time.sleep(15)

            if not AutoGuiUtil.findImg(haoyou):
                LogUtil.logger.info("点击完未找到好友列表")
                time.sleep(15)
                startJiyang()
            lists = [gouyu76, gouyu67, gouyu59, gouyu50, douyu6, douyu5]
            for cardItem in lists:
                if findResource(cardItem):
                    LogUtil.logger.info("完成寄养")
                    global jiyangSuccess
                    jiyangSuccess = True
                    break
                for i in range(30):
                    pyautogui.scroll(1)
            return False
        pass
    except Exception as e:
        LogUtil.logger.error("startJiyang error %s" % e)



def task():
    while 1:
        if AutoGuiUtil.findImg(reject):
            print("多线程 发现任务")
            LogUtil.logger.info("多线程 发现任务")
            AutoGuiUtil.clickImg(reject)
        print("未发现邀请")
        time.sleep(5)


def startJiyangTest():
    time.sleep(30)
    global jiyangSuccess
    jiyangSuccess = True


if __name__ == '__main__':
    startJiyang()
