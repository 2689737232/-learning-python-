#  py中的变量不存储数据，只指向空间。py中处理的所有数据都是对象。
# 内置对象中有许多都可以为开发者所使用，如数字、字符串、列表、del，
# 非内置对象需要导入，如正弦函数sin(x)、数据产生函数random

# 可以为多个变量赋值
a, b, c = 15, "xxx", True
# 用于删除a的引用
del a
# 打印报错，a没有定义
# print(a,b,c)

# py的输出
print("输出后可以通过添加参数end=", end="\n************\n************\n")

# py中的字符串索引从左到右是0开始，
#  从右至左是-1开始
str = "我是Python中的字符串"
print(str[0])
print(str[1])
# py中的字符串截取
# 第一个和第二个参数是起末位置，第三个参数用于截取位置
print(str[0:5:3])

# py中的列表
arr = ["yes", "no", 45, {"a": "对象"}]
print("yes" in arr)
print(arr[3]["a"])

# py中的元祖
#     元组是另一个数据类型，类似于 List（列表）。
#     元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('第一个元组元素', 786, 2.23, 'john', 70.2)
print(tuple[0])
# 尝试更改元组信息，报错
# tuple[0] = "尝试更改"

# py中的字典
#      字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#      两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#      字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
lala = {
    "name": "dictionary",
    "age": 21
}
print(lala["name"])


# py中的数据类型转换
#         int(x [,base])
#         将x转换为一个整数
#         long(x [,base] )
#         将x转换为一个长整数
#         float(x)
#         将x转换到一个浮点数
#         complex(real [,imag])
#         创建一个复数
#         str(x)
#         将对象 x 转换为字符串
#         repr(x)
#         将对象 x 转换为表达式字符串
#         eval(str)
#         用来计算在字符串中的有效Python表达式,并返回一个对象
#         tuple(s)
#         将序列 s 转换为一个元组
#         list(s)
#         将序列 s 转换为一个列表
#         set(s)
#         转换为可变集合
#         dict(d)
#         创建一个字典。d 必须是一个序列 (key,value)元组。
#         frozenset(s)
#         转换为不可变集合
#         chr(x)
#         将一个整数转换为一个字符
#         unichr(x)
#         将一个整数转换为Unicode字符
#         ord(x)
#         将一个字符转换为它的整数值
#         hex(x)
#         将一个整数转换为一个十六进制字符串
#         oct(x)
#         将一个整数转换为一个八进制字符串

"""
    多行注释
"""

print(4 is not 8)
print(4 is 4)
print(4 is "4")
#  id() 函数用于获取对象内存地址。
print(id(4))
a = "yes"
if a == "yes":
   print("对的哦 我的宝贝")



