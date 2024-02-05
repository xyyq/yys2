import random
import string

import pyautogui
import time
import xlrd
import pyperclip
import AbstractChallengeClass
from abc import ABC, abstractmethod






success = 1






def challenge():
    for x in range(180):
        print('start times : {}'.format(x + 1))
        # 先点挑战 尝试3次
        for challenge in range(5):
            print("尝试挑战 : {}".format(challenge + 1))
            res = clickChallenges()
            if res:
                # 点到了挑战 休息40s
                #
                print("挑战成功次数 ： {}".format(success))
                success += 1
                time.sleep(60)
                # 屏幕中间间隔3s点三次 保证出来
                break
            # 挑战成功 随机点击
            clickDouble()


# 任务
def clickChallenges():
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

    for i in range(3):
        m = m + random.randint(-50, 50)
        n = n + random.randint(-50, 50)
        pyautogui.click(m / 2, n / 2, clicks=2, interval=0.2, duration=0.1, button="left")
        print("随机点击 {} 次".format(i + 1))
        time.sleep(2)
        # 点击屏幕中间
