a = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
sum = 0
i = 0
pingjun = 0
while 1 :
    sum += a[i]
    pingjun = sum /8
    i+=1
    if i==8 :
        print("总和为","%.2f"%sum)
        print("平均为","%.2f"%pingjun)
        break

