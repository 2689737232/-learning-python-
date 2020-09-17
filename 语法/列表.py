import random
li = [45, 8, 96, 5, "倒数第二", "倒数第一"]
# -1为list的最后一个元素
print(li[-1])
print(li[-2])

li.append("添加最后一个数据")
li.append([22])
li.insert(0, "往前添加一根数据")
# 返回第一个96的下标
li.index(96)
# 删除第一个
li.pop()
li.reverse()
print(li)

x = list(range(11))
random.shuffle(x)
print(x)

# 同样list也适用运算符
a = [4, 8, 99, 66, 52]
a += [88]
print(a)

# enumerate
print(list(enumerate(range(4)))) 

# in 判断元素是否在list中  True 或 False
print(88 in a)

# 列表推导式
newLi = [45, 89, 6, 23, 1, 58, 223, 36]
print(sum(newLi))
heightLi = [a for a in newLi if a > 30]
"""
相当于 
height = []
for a in newLie:
   if a > 30:
      height.append(a)
"""
print(heightLi)

# 嵌套循环
list1 = [[55, 88, 99, 66, ], [88, 99, 66, 3, 56], [96, 53, 1553, 53, 6]]
list2 = [b for a in list1 for b in a if b > 30]
print(list2)

# 函数
def handle(v):
   if v > 30:
      return v
   else:
     ""   
list3 = [handle(b) for a in list1 for b in a ]
print(list3)

# 切片 
# [0:10:1] [start,end,step]  左闭右开
list4 = [b for a in list1 for b in a][0:10:1];
list5 = [b for a in list1 for b in a][0:-5:-1];
print(list4)