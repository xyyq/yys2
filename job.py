import datetime

import pyautogui
import schedule
import time


import AutoGuiUtil
import LogUtil
import jiyang
from threading import Thread

import logging
import logging.config

# 加载配置
logging.config.fileConfig(r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\config\logging.conf')

# 创建 logger
logger = logging.getLogger()
jiejieFlag = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\jiejieFlag.png'

reject = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\reject.png'
accept = r'C:\Users\VIVIANIYQ\PycharmProjects\yys2\resource\yys\accept.png'


def job():
    logger.info("这是我的定时任务")
    jiyang.startJiyang()


# 每隔5分钟运行一次job函数
schedule.every(340).minutes.do(job)


def task():
    while 1:
        if jiyang.jiyangSuccess:
            LogUtil.logger.info("寄养完成，多线程结束")
            return
        if AutoGuiUtil.findImg(reject):
            logger.info("多线程 发现任务")
            now = datetime.datetime.now()
            if now.hour < 6:
                AutoGuiUtil.clickImg(reject)
            else:
                AutoGuiUtil.clickImg(accept)
        logger.info("多线程未发现任务")
        time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=task)
    # 启动
    t1.start()
    while True:
        # 等待1秒钟
        time.sleep(10)
        print("kaishi")
        AutoGuiUtil.clickCurrent()
        # 如果当前时间到达设置的定时任务时间点，则调用对应的函数
        schedule.run_pending()
