#  数字、字符串等可hash的可以做建
import random
import string
str = "myKey"
d = {
    45: "可以左键",
    str: "可以添加变量"
}
print(d[45])
print(d[str])

# dict 转化
keys = ["lala", "yeye", "wawa"]
values = [45, 88, 666]
list1 = list(zip(keys, values))
d2 = dict(list1)
print(d2)

# 取键、值
print(d2.keys())
print(d2.values())

#
# 字母、数字、符号
str = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(str) for i in range(1000)]
z = ''.join(y)
d = dict()
for c in z:
    d[c] = d.get(c, 0) + 1

# 删除 pop del
obj = {
    "first": "哇 很有精神",
    "name": "lala",
    "age": 21,
    "hobby": "play game",
    "last": "我淦 我简直帅得不像话",
    "ugly": "丑"
}
obj.pop("first")
del obj["ugly"]
print(obj)

# 查询
print(obj.keys())
print(obj.values())
for key in obj:
    print(obj[key])

# 使用 sort
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
# 按首字母排序  但是会修改cars本来的顺序
cars1.sort()
cars1.sort(reverse=True)
print(cars1)
# 不修改  作为临时的
print(sorted(cars2), cars2)



d = {"key":88,"lala":"a"}
d.get("4444","默认值，如果字典中没有这个值的话，返回我")