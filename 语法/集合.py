# 集合无序、可变。  集合中的每个元素都唯一  
# 集合主要用作 【和 交 并 差】 作用
# 两种创建方式
s = {45,9}
print(type(s))

ss = set(list(range(4)))
print(ss)

# 数组去重
list1 = [44,555,99,6,9,6,9,69,6,22,888,666]
set1 = set(list1)
# 添加 移除
set1.add(444)
set1.remove(555)
print(set1)

# 并集操作
set2 = {45,8,99,66,66,25,25,14}
set3 = {45,88,66,99,66,55,25}
#    第一种操作
set4 = set2 | set3
print(set4)
#    第二种操作
set5 = set2.union(set3)
print(set5)

# 交操作
set6 = set2 & set3
set7 = set2.intersection(set3)

# 差操作
set8 = set2.difference(set3)

