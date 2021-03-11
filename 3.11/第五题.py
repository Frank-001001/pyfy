List = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
b = sorted(List)
c = dict()
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)
