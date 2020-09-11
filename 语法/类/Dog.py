# 导入类
from Animal import Animal
#  创建类  传入父类实现继承
class Dog(Animal):
   # 初始化函数 构造函数 __init__  添加__下划线是为了区分和普通函数的区别
   # 隐式的返回一个实例
   def __init__(self, name, age, color):
      super().__init__(name, age, color)
      #  默认值
      self.style = "cute"

   def set_age(self, age=0):
      if age < 0 or age > 20:
         print("You can't set this invalid value")
      self.age = age

   def roll_over(self):
      print("rolled over!")
      

yellow_dog  = Dog("y",1,"yellow")
yellow_dog.sya_hi()
print(yellow_dog.age,yellow_dog.color,yellow_dog.height)
print(type(yellow_dog))
print(isinstance(yellow_dog,Dog))
# 修改属性
yellow_dog.age = 2 
yellow_dog.set_age(0)
