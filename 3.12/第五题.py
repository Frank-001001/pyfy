def bubbleSort(a):
    n = len(a)

    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
bubbleSort(a)
print("排序后的数组:")
for i in range(len(a)):
    print("%d" % a[i]),