import random
import random as randomObj
import math

print(randomObj.random())
i = 45
print(type(i))
x = '''三引号 '''
dictionary = {
    "name": "lala",
    "age": 21
}
print(dictionary.get("name"))
lala = {
    "name": "lala"
}
x = 2
print(x ** 8)
print(isinstance(3, int))
print(7 < 8 > 5)

l = ['lala', 45, {"name": "yes"}, ('55', "innerData")]
for p in l:
    print(p, type(p))

for v in range(0, 10):
    print(v)
numbers = list(range(1, 6, 2))
print(numbers)


s = []
for v in range(1, 15):
    s.append(v**2)
print(s)
print(max(s))
print(min(s))

# 切割列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
del players[4]
print(players[0:3])
# 没指定开始位置，默认从0开始
print(players[:3])
# 同样没指定结尾 默认到最后
print(players[2:])
# 在for循环中使用切片
for p in players[:3]:
    print(p)

# 通过切片复制列表
copyPlayers = players[:]
copyPlayers[1] = "lala"
print(copyPlayers, players)

isRuning = True
myNum = math.floor(random.random() * 101)

print("*****************猜数字游戏***********************")
while isRuning:
    inp = input("请输入一个数字在0到100间:")
    if bool(1 - isinstance(inp, int)):
        print("滚 get off! ")
        break
    num = int(inp)
    if num > 100 or num < 0:
        print("滚 get off! ")
        break
    if num > myNum:
        print("****************你输入的数字大了******************")
    elif num < myNum:
        print("****************你输入的数字小了******************")
    else:
        isRuning = False
        print("♂♂♂♂♂♂对了我的♂宝贝儿♂♂♂游戏结束♂♂", num, "♂♂♂♂♂♂♂♂♂♂")
print("****************游戏结束************************")


# 字典
d = {
    "name": "lala",
    "age": 21,
    "data": {
        "value": 666
    }
}
for p in d:
    print(p.title())

import func
from func import cl_

func.cl_(88,"88",{"name":"args"})



