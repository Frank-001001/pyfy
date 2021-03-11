i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d"%(i,j,i*j),end = ' ')  # %d： 整数的占位符，'-2'代表靠左对齐，两个占位符
        j += 1
    print()
    i += 1