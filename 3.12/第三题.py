import sys
import random

print("-------欢迎来到德莱联盟-------")
user = "root"
psw = "password"
n = 0
jifen = 0
youhuijiage = 0
youhuiquan = ["免单券", "免单券", "免单券", "免单券", "免单券", "免单券",
              "免半券", "免半券", "免半券",
              "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券",
              "满600减100券", "满600减100券",
              "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券",
              "满600减100券", "满600减100券",
              "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券",
              "满600减100券", "满600减100券",
              "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券",
              "满600减100券", "满600减100券",
              "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券", "满600减100券",
              "满600减100券", "满600减100券",
              "满10000减1000券", "满10000减1000券", "满10000减1000券", "满10000减1000券", "满10000减1000券", "满10000减1000券",
              "满10000减1000券", "满10000减1000券", "满10000减1000券", "满10000减1000券",
              "无券"]
while 1:
    yonghu = input("请输入用户名")
    mima = input("请输入密码")
    if yonghu == "root" and mima == "password":
        print("成功登录系统，开始您的购物")
        break
    else:
        print("用户名或密码输入错误请重新输入")
        n += 1
        if n == 3:
            print("系统关闭")
            sys.exit()
gold = int(input("请输入您的金钱"))
gold1 = gold
yhq = youhuiquan[random.randint(0, len(youhuiquan) - 1)]
print("恭喜您获得了：", yhq)
shop = [["老干妈", 34], ["意大利炮", 90], ["awsl", 100], ["手办", 98], ["小天才", 500], ["are you ok ", 90000], ["肖战必糊", 1]]
shopcar = []

while 1:
    for index, value in enumerate(shop):
        print(index, value)
    i = (input("请输入商品编号"))
    if i.isdigit():
        i = int(i)
        if i in range(len(shop)):
            if gold >= shop[i][1]:
                shopcar.append(shop[i])
                gold -= shop[i][1]
                jifen += shop[i][1]
                print("\033[32;20;1m若购买此商品！您的余额为：", gold, "￥ ", "您的积分为", jifen, "\033[0m")
            else:
                print("\033[41;20;1m你噶了，穷鬼！\033[0m")
        else:
            print("怎么回事小老弟")
    elif i == "q" or i == "Q":
        print("下次光临")
        break
    else:
        print("你在开玩笑呢")
print("您的购买内容为：")
for index, value in enumerate(shopcar):
    print(index, ":", value)
youhuijiage = jifen
if yhq == "免单券":
    youhuijiage = 0
elif yhq == "满600减100券":
    if youhuijiage < 600:
        print("您不能使用此券")
    else:
        youhuijiage -= 100
elif yhq == "满10000减1000券":
    if youhuijiage < 10000:
        print("您不能使用此券")
    else:
        youhuijiage -= 1000
else:
    print("无优惠")
print("------------您获得了：", yhq, "")
print("------------使用优惠券之后价格为：", youhuijiage, "￥！")
print("------------您的余额：", youhuijiage, "￥！", "您的积分为", jifen, "------------------")
