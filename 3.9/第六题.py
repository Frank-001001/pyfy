import  time
user = 123
password1 = 456
i = 0
while 1 :
    x = input("输入用户名")
    y = input("输入密码")
    if user == x and password1 == y :
        print("验证通过")
    else:
        print("输入错误再次输入")
    i += 1
    if i == 3 :
        print("你噶了")
        while 1 :
            time.sleep(1)




