class Animal:

    def eat(self):
        print("吃--")

    def drink(self):
        print("喝--")

    def run(self):
        print("跑--")

    def sleep(self):
        print("睡--")


class Dog(Animal):

    # 子类拥有父类的所有属性和方法
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):

        # 1. 针对子类特有的需求，编写代码
        print("叫的跟神一样")

        # 2.使用 super(). 调用原本封装在父类中的方法
        super().bark()

        # 父类名.方法(self)(python2.0中)
        # Dog.bark(self)
        # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
        # XtianTianQuan.bark(self)

        # 3.增加其他子类方法
        print("！@#￥%……&*")


xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
