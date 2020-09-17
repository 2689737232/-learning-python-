# 元组 定义后不能修改，要不就转化为list修改后再转为元组
#     用于查找，访问速度快。可以对元组进行切片，但是切片后不能修改。
wa = (4,8,9,6,55,6)
# 如果是一个元素的元组必须要加逗号,如果不加逗号，会变成这个元素
only = (45,)

# 生成器 迭代器
g  = (a for a in wa)
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g))
 