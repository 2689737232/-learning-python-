# py中的函数
import keyword
# 可以添加默认值操作
def lala(type = "int"):
   if type == "int":
      v = int(input("输入一个数"))
   print(v)
   return v

v =  lala()
print(keyword.kwlist,v)

# 收集操作
def cl_(*all_args):
   print(all_args)
   print(type(all_args))
   
# cl_(45,"44",{"name":"lala"})     


str = input("输入一个数字字符串")
a,b,c = map(int,str)
print(a,b,c)
