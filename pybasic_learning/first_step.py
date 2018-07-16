# coding=utf-8
# this is my first python exercise, fucking cool!

import math

# list
name = ['haha', 'haha', 'jianyang', [23, 12.2], True, {'haha': 90, 12: True}, {1, 2, 22, 2}]
name1 = [(1, 'eval'), (2, 'train')]

# tuple
tname = (('haaha', 'janeyang'), 'liuliu', 23, {'haha': 90, 12: True})
tname1 = ('lu', 23, ['kangkang', True], 'hhe')

# dict
dname = {'jane': 12, 'yang': 66, 'kang': ['dsgad', 'ka'], 'Maria': {23: 'lulu', 21: "haha", 16: 'xixi'},
         'Momo': ('m', 'o', 15)}
dname.get('Maria').get(21)

# set
# 和dict一样，作为key的对象为不可变对象，且不能重复
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   TypeError: unhashable type: 'list'
# sname = {12, 22, 'dsad', True, 22, (1, 2, 3), {9: 'lalla', 8: 'poli'}, ['jjs', 'jrs']}

num = dname.keys()

# test loop
# sum = 0
# for x in range(101):
#     sum = sum + x

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x


# function test
def my_first_fun(x, y):
    if not isinstance(x, (int, float)):
        raise TypeError('are you fucking kidding me !!')
    if not isinstance(y, float):
        raise TypeError('are you fucking kidding me !!')
    if y < 10:
        print('hello %s %s' % (x, y))
    elif x > y:
        return abs(x - y)
    elif x <= y:
        return abs(y - x)
    else:
        return


def power(x):
    return x * x


# 默认参数
# 设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def tpower(x, n=2):
    if not isinstance(x, int):
        raise TypeError('are you fucking kidding me !')
    total = 1
    while n > 0:
        total = total * x
        n = n - 1
    return total


def enroll(name, gender, age=6, city='Beijing', tele='123456'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
    print 'tele:', tele


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    print("L:", L)
    return L


def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 定义可变参数
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    s = 1
    for n in numbers:
        s = s + n * n
    return s


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def staff(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


# 递归函数
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# 改进
def fact_fix(n, product=1):
    if n == 1:
        return product
    else:
        return fact_fix(n - 1, n * product)


# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且！return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# return fact_iter(num - 1, num * product)仅返回递归函数本身，
# num - 1和num * product在函数调用前就会被计算，不影响函数调用。
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 构造1-99的数表
def consnums():
    # num = 0
    # nums = []
    # while num < 100:
    #     nums.append(num)
    #     num += 1
    nums = range(100)
    return nums


if __name__ == '__main__':
    pass
    # print(num)
    # print sum
    # k = my_first_fun(True, 66.66)
    # print(k)

    # print(tpower(2, 5))
    #
    # enroll('haha', 'M', tele='123266666')

    # l = add_end()
    # lp = add_end()      # 在L中累计
    # li = add_end([12, 'haha'])
    # l1 = add_end1()
    # lp1 = add_end1()    # 调用时，重新初始化
    # li1 = add_end1([12, 'haha'])
    # print 'l:', l, 'lp:', lp, 'li:', li
    # print 'l1:', l1, 'lp1:', lp1, 'li1:', li1

    # print(fact(1000))

    # numl = [1, 2, 3]
    # print(calc(1, 2, 3))
    # print(calc(*numl))

    # staff('xiaoming', 12, tele='12345678')
    # kw = {'city': 'Beijing', 'job': 'Engineer'}
    # staff('haha', 15, **kw)

    # print(fact1(5))

    # print(consnums())
