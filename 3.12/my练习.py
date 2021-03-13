print("-------欢迎来到德莱联盟-------")
gold=int(input("请输入您的金钱"))
shop=[["老干妈",34],["意大利炮",90],["awsl",100],["手办",98],["小天才",500],["are you ok ",90000],["肖战必糊",1]]
shopcar=[]
while 1 :
    for index, value in enumerate(shop):
        print(index, value)
    i =(input("请输入商品编号"))
    if i.isdigit ():
        i=int(i)
        if i in range(len(shop)) :
            if gold >=shop[i][1]:
                shopcar.append(shop[i])
                gold -=shop[i][1]
                print("\033[32;20;1m购买成功！您的余额为：", gold, "￥！\033[0m")
            else:
                print("\033[41;20;1m你噶了，穷鬼！\033[0m")
        else:
            print("怎么回事小老弟")
    elif i =="q" or i== "Q":
        print("下次光临")
        break
    else:
        print("你在开玩笑呢")
print("您的购买内容为：")
for index,value in enumerate(shopcar):
    print(index,":",value)
print("------------您的余额：",gold,"￥！------------------")