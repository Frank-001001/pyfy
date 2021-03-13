names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
name1 = []
name2 = []
man = 0
girl = 0
new = []
i = 0
while i < len(names):
    name1.append(names[i][-2])
    name2.append(names[i][1])
    for x in names[i][2]:
        if x == "男":
            man += 1
        else:
            girl += 1
    i += 1
name2 = [int(x) for x in name2]
print("平均薪资为", float((sum(name1) / len(names))))
print("平均年龄", (float(sum(name2)) / len(names)))
i = 0
while i < 7:
    new.append(input("请输入新员工的信息："))
    i += 1
names.append(new)
i = 0
for i in range(len(names) - 1):
    flag = 0
    for j in range(i):
        if names[j][-1] == names[i][-1]:
            flag = 1
            break
    if flag == 1:
        continue  # 跳过到下一轮循环
    counter = names[i][-1].count(names[i][-1])
    print(names[i][-1], "出现了", counter, "次！")
print(names)
print("男生人数", man, "女生人数", girl)
