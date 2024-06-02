from abc import ABC, abstractmethod
import random
import string
import enum

import pyautogui
import time
import xlrd
import pyperclip

th28 = pyautogui.Point(x=922, y=535)
tansuo = pyautogui.Point(x=769, y=586)
cancel = pyautogui.Point(x=837, y=274)
exit = pyautogui.Point(x=44, y=108)
confirm = pyautogui.Point(x=607, y=468)
nextScene = pyautogui.Point(x=972, y=701)

challenge = pyautogui.Point(x=975, y=764)
invite = pyautogui.Point(x=617, y=487)

class AbstractChallengeClass(ABC):
    times = 1
    interval = 100

    point = pyautogui.position(0,  0)


    def setTimes(self, times):
        self.times = times


    def setPoint(self, x , y):
        self.point = pyautogui.position(x,  y)
    def setInterval(self, interval):
        self.interval = interval

    @abstractmethod
    def challenge(self):
        pass

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def getImg(self):
        pass


# 子类必须实现所有抽象方法才能被实例化
class Hun11ConcreteClass(AbstractChallengeClass):

    def challenge(self):
        print("times:".format(self.times))
        realChallenge(self.times, self.interval, self.getImg(), self.point)

    def getType(self):
        return "魂土"

    def getImg(self):
        return "/Users/sifatasinant/Downloads/hun11.PNG"


# 子类必须实现所有抽象方法才能被实例化
class ActivityConcreteClass(AbstractChallengeClass):

    def challenge(self):
        print("times:".format(self.times))
        success = 1
        realChallenge(self.times, self.interval, self.getImg(), self.point)

    def getType(self):
        return "活动"

    def getImg(self):
        return "/Users/sifatasinant/Downloads/cong.PNG"


# 子类必须实现所有抽象方法才能被实例化
class DifficultConcreteClass(AbstractChallengeClass):

    def challenge(self):
        print("times:".format(self.times))
        success = 1
        difficultChallenge(self.times, self.interval, self.getImg())

    def getType(self):
        return "困28"

    def getImg(self):
        return "/Users/sifatasinant/Downloads/challenge.PNG"



# 子类必须实现所有抽象方法才能被实例化
class MutiDifficultConcreteClass(AbstractChallengeClass):

    def challenge(self):
        print("times:".format(self.times))
        success = 1
        mutiDifficultChallenge(self.times, self.interval, self.getImg())

    def getType(self):
        return "困28组队"

    def getImg(self):
        return "/Users/sifatasinant/Downloads/challenge.PNG"


# 任务
def clickChallenge(img, confidence):
    # 取本行指令的操作类型
    # 取图片名称
    # 找图
    # 找到挑战，
    # 点击挑战
    # 点完挑战 挑战图片没了
    #
    if challengeSuccess(img, confidence=confidence):
        return True
    return False


def clickDouble():
    m, n = pyautogui.size()

    m += 300
    n -= 300

    for i in range(2):
        m = m + random.randint(-50, 50)
        n = n + random.randint(-50, 50)
        pyautogui.click(m / 2, n / 2, clicks=2, interval=0.2, duration=0.1, button="left")
        print("随机点击 {} 次".format(i + 1))
        time.sleep(1)
        # 点击屏幕中间
    time.sleep(random.randint(50, 100) * 0.03)



def clickDouble(point):

    for i in range(2):
        pyautogui.click(point.x + random.randint(50,100) * 0.1 , point.y + random.randint(50,100) * 0.1, clicks=2, interval=0.2 + random.randint(1,2) * 0.1, duration=0.1, button="left")
        print("随机点击 {} 次".format(i + 1))
        time.sleep(random.randint(50,100) * 0.03)
        # 点击屏幕中间
    time.sleep(random.randint(50, 100) * 0.03)


def challengeSuccess(img, confidence):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=confidence)
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
        print("未找到图片 ", img)
        print(e)
        return False


def realChallenge(times, interval, img, point):
    print("times:{}".format(times))
    print("interval:{}".format(interval))
    print("img:{}".format(img))
    success = 1

    for x in range(int(times)):
        print('start times : {}'.format(x + 1))
        # 先点挑战 尝试3次
        for challenge in range(5):
            print("尝试挑战 : {}".format(challenge + 1))
            res = clickChallenge(img, 0.9)
            if res:
                # 点到了挑战 休息40s
                print("挑战成功次数 ： {}".format(success))
                success += 1
                time.sleep(int(interval))
                # 屏幕中间间隔3s点三次 保证出来
                break
            # 挑战成功 随机点击
            clickDouble(point)


def clicksImg(img, interval, confidence):
    click = False
    try:
        for i in range(interval):
            location = pyautogui.locateCenterOnScreen(img, confidence=confidence)
            # 先左键点击挑战
            pyautogui.click(location.x / 2, location.y / 2, clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
                            duration=0.3 + random.randint(-10, 10) / 100, button="left")
            print("单击左键", img)
            time.sleep(3)
            clickDouble()
            click = True
    except Exception as e:
        print("未找到图片", img)
        print(e)
        return click


def clickImg(img):
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
        # 先左键点击挑战
        pyautogui.click(location.x / 2, location.y / 2, clicks=4, interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        print("单击左键", img)
        time.sleep(0.5)
        return True

    except Exception as e:
        print("未找到图片", img)
        print(e)
        return False


def moveTo(img):
    try:
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.6)
        # 先左键点击挑战
        x = x / 2 + 110
        y = y / 2 - 30
        pyautogui.click(x, y, clicks=2,
                        interval=0.4 + random.randint(-10, 10) / 100,
                        duration=0.3 + random.randint(-10, 10) / 100, button="left")
        print("单击左键", img)
        time.sleep(0.5)
        return True

    except Exception as e:
        print("未找到移动图片")
        print(e)
        return False
    pass


def findImg(img):
    try:
        pyautogui.locateCenterOnScreen(img, confidence=0.8)
        # 先左键点击挑战
        return True
    except Exception as e:
        print("未找到图片", img)
        print(e)
        return False


def my_click(point):
    pyautogui.click(point.x + random.randint(-5, 5), point.y + random.randint(-5, 5), clicks=1,
                    interval=0.4 + random.randint(-10, 10) / 100,
                    duration=0.3 + random.randint(-10, 10) / 100, button="left")
    time.sleep(1)
    return


def tansuo_to_dungeon():
    print("尝试进入副本")
    in_dungeon = findImg("/Users/sifatasinant/Downloads/in_dungeon.PNG")
    if in_dungeon:
        return
    ## 有没有妖气标记
    if findImg("/Users/sifatasinant/Downloads/28tansuo.PNG"):
        my_click(tansuo)
        in_dungeon = findImg("/Users/sifatasinant/Downloads/in_dungeon.PNG")
        if not in_dungeon:
            print("没有进入副本")
            return tansuo_to_dungeon()
    else:
        if findImg("/Users/sifatasinant/Downloads/yaoqi.PNG"):
            ##点击28th
            my_click(th28)
            ##点击探索
            my_click(tansuo)
            in_dungeon = findImg("/Users/sifatasinant/Downloads/in_dungeon.PNG")
            if not in_dungeon:
                print("没有进入副本")
                return tansuo_to_dungeon()
            return
    return tansuo_to_dungeon()


def search_for_exp(fightCount, interval, img):
    bossChallenge = challengeSuccess(img="/Users/sifatasinant/Downloads/boss.jpeg", confidence=0.7)
    if bossChallenge:
        # 打完boss
        # 领奖励
        print("打完boss")

        fightCount = fightCount + 1
        time.sleep(int(interval))
        clickDouble()
        get_bonus()
        return TansuoResult.FinishedWithBoss

    res = clickImg(img)
    if res:
        # 点到了挑战 休息40s
        fightCount = fightCount + 1
        time.sleep(int(interval))
        clickDouble()
        # 屏幕中间间隔3s点三次 保证出来
        search_for_exp(fightCount, interval, img)

    return TansuoResult.FinishedWithoutBoss


def next_scene():
    ##移动到下一屏
    print("寻找下一屏")
    my_click(nextScene)
    time.sleep(1)


def one_tansuo(interval, img):
    fightCount = 0
    result = search_for_exp(fightCount, interval, img)
    if result == TansuoResult.FinishedWithBoss:
        print('finished with boss')
        time.sleep(1)
        return result
    else:
        next_scene()
        result = search_for_exp(fightCount, interval, img)
        if result == TansuoResult.FinishedWithBoss:
            print('finished with boss')
            time.sleep(1)
            return result
    return TansuoResult.FinishedWithoutBoss


def get_bonus():
    for i in range(3):
        clicksImg(img="/Users/sifatasinant/Downloads/bonus.jpg", interval=3, confidence=0.7)
        time.sleep(1)


def escape():
    my_click(exit)
    my_click(confirm)
def mutiDifficultChallenge(times, interval, img):
    print("times:{}".format(times))
    print("interval:{}".format(interval))
    print("img:{}".format(img))
    success = 0
    while success < int(times):
        my_click(invite)
        my_click(challenge)
        tansuoResult = one_tansuo(interval, img)
        success = success + 1
        if tansuoResult == TansuoResult.FinishedWithoutBoss:
            if findImg("/Users/sifatasinant/Downloads/in_dungeon.PNG"):
                ##还在探索里
                ##先强制退出
                escape()

def difficultChallenge(times, interval, img):
    print("times:{}".format(times))
    print("interval:{}".format(interval))
    print("img:{}".format(img))
    success = 0
    while success < int(times):
        tansuo_to_dungeon()
        tansuoResult = one_tansuo(interval, img)
        success = success + 1
        if tansuoResult == TansuoResult.FinishedWithoutBoss:
            if findImg("/Users/sifatasinant/Downloads/in_dungeon.PNG"):
                ##还在探索里
                ##先强制退出
                escape()
    #
    # for x in range(int(times)):
    #     print('start times : {}'.format(x + 1))
    #     fail = 0
    #     # 先点挑战 尝试3次
    #     for challenge in range(5):
    #         print("尝试挑战 : {}".format(challenge + 1))
    #         bossChallenge = challengeSuccess(img="/Users/sifatasinant/Downloads/boss.jpeg", confidence=0.7)
    #         if bossChallenge:
    #             # 打完boss
    #             # 领奖励
    #             print("打完boss")
    #             time.sleep(int(interval))
    #             clickDouble()
    #             clicksImg(img="/Users/sifatasinant/Downloads/bonus.jpg", interval=3, confidence=0.7)
    #             time.sleep(5)
    #             clickDouble()
    #             click = clicksImg(img="/Users/sifatasinant/Downloads/search.jpg", interval=2, confidence=0.9)
    #             if click:
    #                 clickDouble()
    #                 break
    #             time.sleep(5)
    #
    #             # 再进挑战
    #             clicksImg(img="/Users/sifatasinant/Downloads/28th.jpg", interval=3, confidence=0.8)
    #
    #             time.sleep(5)
    #             # 点击探索
    #             clicksImg(img="/Users/sifatasinant/Downloads/search.jpg", interval=2, confidence=0.9)
    #
    #             break
    #         res = clickImg(img)
    #         if res:
    #             # 点到了挑战 休息40s
    #             print("挑战成功次数 ： {}".format(success))
    #             success += 1
    #             time.sleep(int(interval))
    #             # 屏幕中间间隔3s点三次 保证出来
    #             break
    #         else:
    #             fail = fail + 1
    #             # 没有boss 也有没找到小怪 移动屏幕
    #             if fail >= 2:
    #                 print("移动屏幕")
    #                 moveTo(img="/Users/sifatasinant/Downloads/right.jpg")
    #
    #         # 挑战成功 随机点击
    #         clickDouble()


class TansuoResult(enum.Enum):
    FinishedWithBoss = 0
    FinishedWithoutBoss = 1
