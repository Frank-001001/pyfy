
import random
import time
num = random.randint(0, 10)
gold=0
n=0
asd=20
print("您的初始资金为0")
while 1:
    n+=1
    a = int(input("请输入一个数字："))
    if num > a:
        print("你猜的数字小了")
    elif num < a:
        print("你猜的数字大了")
    elif num==a:
        print("你成功了")
        print("你猜了",n,"次")
        if n<3:
            gold+=200
            print("游戏结束，您的资金为",gold)
        else:
            print("资金不加不减")
        break
    if n==20:
        print("您已经猜了20次了系统需要休息一下")
        while 1:
            time.sleep(1)
            print("还有",asd,"秒")
            asd-=1
            if asd==0:
                break
    elif n==6:
        print("您已经猜了60次了系统锁定")
        while 1:
            time.sleep(1)



