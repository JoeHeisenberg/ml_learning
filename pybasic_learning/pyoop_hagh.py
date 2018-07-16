# coding=utf-8

"""
this module for python higher oop exercise
"""
from types import MethodType

__author__ = 'joe'

"""
属性与方法的动态绑定
"""


class Animal(object):
    # 报错???
    # __slots__ = ('weight', 'distinct')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def bark(self):
        print('%s barking' % self.__name)


class Pig(Animal):

    def __init__(self, name, color, barkType):
        super(Pig, self).__init__(name, color)
        self.__name = name
        self.__color = color
        self.__barkType = barkType

    # 定制(类似于java中的重写toString()方法)
    def __str__(self):
        return 'Pig object (name: %s)' % self.__name

    def bark(self):
        print('%s barking %s' % (self.__name, self.__barkType))


# 由于'sex'没有被放到__slots__中，所以不能绑定sex属性，试图绑定sex将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class Child(object):
    __slots__ = ('name', 'age')

    def __getattr__(self, item):
        if item == 'count':
            return 10

    pass


# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
class Red_Child(Child):
    __slots__ = ('color', 'weight')
    pass


# set_color方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
def set_color(self, color):
    self.color = color


"""
使用@property
"""


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


"""
多重继承(Mixin)
# Mixin的目的就是给一个类增加多个功能，
# 这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。
# 参见:https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200511568dd94e77b21d4b8597ede8bf65c36bcd000
# https://www.jianshu.com/p/dae61c60f323
"""

"""
定制类
"""


# 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


"""
枚举类
"""

"""
元类
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
"""

if __name__ == '__main__':
    pass

    # animal = Animal('daha', 'red')
    # animal2 = Animal('kiki', 'pink')
    # pig = Pig('xixi', 'green', 'hengheng~')
    # animal.bark()
    # pig.bark()

    # animal.__setattr__('weight', '98kg')
    # animal.__setattr__('run', 'running')
    # animal.set_color = MethodType(set_color, animal, Animal)  # 绑定到对象
    # Animal.set_color = MethodType(set_color, None, Animal)  # 通过类绑定,所有实例均获得此方法
    # animal.set_color('yellow')
    # animal2.set_color('dark')

    # print(animal.weight)
    # # print(animal.run)
    # print(animal.color)
    # print(animal2.color)

    # c = Child()
    # c.__setattr__('name', 'child')
    # c.__setattr__('sex', 'male')
    # print c.name, c.sex
    # rc = Red_Child()
    # rc.__setattr__('sex', 'male')
    # print(rc.sex)

    # student = Student()
    # student.score = 100
    # print(student.score)

    # print pig

    # ch = Child()
    # ch.name = 'test'
    # # ch.kii = 'kka'
    # print(ch.count)  # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性

    print(Chain().status.user.timeline.list)
