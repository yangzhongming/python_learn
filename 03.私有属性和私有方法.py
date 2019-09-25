class Woman:
    def __init__(self,name):
        self.name = name
        self.__age = 18;
    def __secret(self):
        print("我的年龄是%d"%self.__age)

xiaomei = Woman("小美")

print(xiaomei._Woman__age)