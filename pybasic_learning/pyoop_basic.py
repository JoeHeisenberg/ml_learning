# coding=utf-8
"""
this module is for python oop exercise.
"""
import types

import builtins
from numpy import unicode

__author__ = 'joe'


# 表示所继承的类是object
class Student(object):
    # 实例属性和类属性(如count定义)
    # 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
    count = 0

    # __init__方法相当于Java类中的构造函数，注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    # 通过在属性字段前加'__'(双下划线)私有化类的变量,只有内部可以访问，外部不能访问;通过提供get/set方法供外界访问
    def __init__(self, name, age, sex, score):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self._score = score
        Student.count += 1

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数。
    def printInfo(self):
        print('%s info:%s,%s,%s' % (self.__name, self.__age, self.__sex, self._score))

    def select(self):
        if 18 > self.__age > 0:
            print('too yong too simple!')
        elif self.__age < 30:
            print('passion man!')
        elif self.__age < 60:
            print('bottle man...')
        else:
            print('time to easy life')


# 继承与多态
# “开闭”原则：
# 对扩展开放：允许新增Person子类；
# 对修改封闭：不需要修改依赖Person类型的run_t()等函数。
class Person(object):
    def run(self):
        print('person run...')


class Manager(Person):
    def run(self):
        print('Manager run...')


class Staff(Person):
    def run(self):
        print('Staff run...')


def run_t(Person):
    Person.run()
    Person.run()


# 获取对象信息,python中所有的变量(变量,函数,对象)均为对象:type()方法
# Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
def getInfo():
    # 所有类型本身的类型就是TypeType
    print(type(str))
    print(type(str) == type(int) == types.TypeType)
    # 要判断class的类型，可以使用isinstance()函数。
    # 能用type()判断的基本类型也可以用isinstance()判断：
    # 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
    print(isinstance(m, Person))
    # 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
    print(isinstance('a', (str, unicode)))
    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    lscontent = dir(__builtin__)  # 获取python内置module中的属性和方法
    for n in lscontent:
        if n == 'dir':
            print(lscontent)


if __name__ == '__main__':
    pass

    stu = Student('haha', 15, 'male', 98)
    # 和静态语言不同，Python允许对实例变量绑定任何数据，
    # 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
    # stu._score = 54
    # stu.printInfo()
    # stu.select()

    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    # 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
    # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name,(不同版本的Python解释器可能会把__name改成不同的变量名。)
    # 所以，仍然可以通过_Student__name来访问__name变量：
    # print(stu._Student__name)
    # 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，(虽然Idea编辑器环境'stu.'候选项中无此属性)
    # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    # print(stu._score)

    # p = Person()
    m = Manager()
    # run_t(p)
    # run_t(m)

    getInfo()

    # if Student.count != 0:
    #     print('测试失败!')
    # else:
    #     bart = Student('haha', 15, 'male', 98)
    #     if Student.count != 1:
    #         print('测试失败..!')
    #     else:
    #         lisa = Student('haha', 15, 'male', 98)
    #         if Student.count != 2:
    #             print('测试失败...!')
    #         else:
    #             print('Students:', Student.count)
    #             print('测试通过!')
