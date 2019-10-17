class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s蹦蹦跳跳的玩耍"%self.name)

class Xiaotianquan(Dog):
    def game(self):
        print("%s飞到天上去玩耍"%self.name)

class Person:
    def __init__(self,name):
        self.name = name
    def go_with_dog(self,dog):
        print("%s和%s快乐的玩耍"%(self.name,dog.name))
        dog.game()

wangcai = Dog("旺财")
wangcai = Xiaotianquan("飞天旺财")
xiaoming = Person("小明")
xiaoming.go_with_dog(wangcai)
