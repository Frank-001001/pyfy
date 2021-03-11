a=["北京","上海","广东"]
while 1:
    i=input()
    a.append(i)
    if i == "结束" :
        a.remove("结束")
        print(a)
        continue
    elif i == "修改" :
        a.remove("修改")
        a.remove("广东")
        a.insert(1,"广东")
        print(a)
