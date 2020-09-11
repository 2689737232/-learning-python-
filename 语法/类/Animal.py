class Animal():
    def __init__(self, name, age, color):
        super().__init__()
        self.name = name
        self.age = age
        self.color = color
        self.height = 50

    def sya_hi(self):
        print("My name is " + self.name + " and i love you my master.")
