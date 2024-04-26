import random
import string

import pyautogui
import time
import xlrd
import pyperclip

from AbstractChallengeClass import *


def challengeSuccess(img):

    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # 先左键点击挑战
        pyautogui.click(location.x / 2, location.y / 2, clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        print("单击左键", img)
        time.sleep(0.5)
        try:
            pyautogui.locateCenterOnScreen(img, confidence=0.9)
            print("点击完挑战还有挑战按钮，挑战无效")
            return False
        except Exception as e:
            print("挑战成功")
            return True
    except Exception as e:
        print("未找到挑战按钮 ")
        print(e)
        return False




# 找图
# 找到挑战，
# 点击挑战
# 点完挑战 挑战图片没了
#


# 任务
def clickChallenge():
    # 取本行指令的操作类型
    # 取图片名称
        img = "/Users/sifatasinant/Downloads/gold.jpg"

        # 找图
        # 找到挑战，
        # 点击挑战
        # 点完挑战 挑战图片没了
        #
        if challengeSuccess(img):
            return True
        return False



def clickDouble():
    m, n = pyautogui.size()

    m += 100
    n += 100

    for i in range(2):
        m = m + random.randint(-50, 50)
        n = n + random.randint(-50, 50)
        pyautogui.click(m / 2, n / 2, clicks=2, interval=0.2, duration=0.1, button="left")
        print("随机点击 {} 次".format(i + 1))
        time.sleep(1)
        # 点击屏幕中间


success = 1

if __name__ == '__main__':
    i = 1
    challengeMaps = {Hun11ConcreteClass.getType(self= Hun11ConcreteClass): Hun11ConcreteClass(),
                     ActivityConcreteClass.getType(self= ActivityConcreteClass): ActivityConcreteClass(),
                     DifficultConcreteClass.getType(self= DifficultConcreteClass) : DifficultConcreteClass(),
                     MutiDifficultConcreteClass.getType(self=MutiDifficultConcreteClass): MutiDifficultConcreteClass()

                     }
    print("开始选择")
    a = pyautogui.confirm(text='挑战类型', title='请选择挑战的内容', buttons=["魂土","困28","困28组队","活动"])  # 10个按键0-9的消息弹窗
    challengeClass = challengeMaps.get(a)
    print(type(challengeClass))
    times = pyautogui.prompt(text='挑战次数', title='请选择挑战次数', default = 30)  # 10个按键0-9的消息弹窗
    challengeClass.setTimes(times)
    interval = pyautogui.prompt(text='挑战间隔', title='挑战间隔', default = 60)  # 10个按键0-9的消息弹窗
    challengeClass.setInterval(interval)
    challengeClass.challenge()



