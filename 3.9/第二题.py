a = 1
sum1 = 0
zuida = 0
pingjun = 0
while a <= 10:
    b: int = int(input())
    sum1 += b
    print(b)
    pingjun = sum1 // 10
    a += 1
    if b > zuida:
        zuida = b
        continue
print("和为" , sum1)
print("平均为",pingjun)
print("最大数为",zuida)
