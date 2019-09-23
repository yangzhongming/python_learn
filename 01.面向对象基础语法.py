class Cat:

    def __init__(self,name):
        self.name = name
        print("初始化方法...")
    def eat(self):
        print("%s 爱吃鱼" %self.name)
    def drink(self):
        print("%s 爱喝鱼汤"%self.name)
    def __str__(self):
        return "我是小猫%s" %self.name

tom = Cat("Tom")
tom.eat()
tom.drink()
print(tom)

jerry = Cat("jerry")
# jerry.name = "jerry"
jerry.eat()
jerry.drink()

print(tom==jerry)