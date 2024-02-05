import random
import string

import pyautogui
import time
import xlrd
import pyperclip


# 定义鼠标事件

# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159


success = 1

if __name__ == '__main__':

    i = 1
    pyautogui.confirm(text='挑战类型', title='请选择挑战的内容', buttons=["魂土", "活动"])  # 10个按键0-9的消息弹窗

    a = pyautogui.confirm(text='挑战类型', title='请选择挑战的内容', buttons=["魂土", "获得"])  # 10个按键0-9的消息弹窗




    for x in range(180):
        print('start times : {}'.format(x + 1))
        # 先点挑战 尝试3次
        for challenge in range(5):
            print("尝试挑战 : {}".format(challenge + 1))
            res = clickChallenge()
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








