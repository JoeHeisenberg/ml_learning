# coding=utf-8
# this file is for functional programing

import functools

_author_ = 'joe'


# 1 map reduce


def str2num():
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, '13579'))


def num2chen(L=None):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


# 2 filter
# python 中的and从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值。
# or也是从左到右计算表达式，返回第一个为真的值。
def sp_filter(L=None):
    def not_empty(s):
        return s and s.strip()

    return filter(not_empty, L)


# 3 sorted
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


def sort(L=None):
    return sorted(L, reversed_cmp)  # reverse=True


def sort_ignore(L=None):
    return sorted(L, cmp_ignore_case)


# 4 函数作为返回值
# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数summ时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
def lazy_sum(*args):
    def summ():
        value = 0
        for n in args:
            value += n
        return value

    return summ


# def lazy_sum1(*args):
#     def summ():
#         value = 0
#         for n in args:
#             def mid(j):
#                 def l():
#                     value += j
#         return value
#
#     return summ


# 比较
# 返回的函数并没有立刻执行，而是直到调用了f()才执行
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，！它们！所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
        # print(fs)
    return fs


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count1():
    fs = []
    for i in range(1, 4):
        def f(j):  # （即将共同引用的循环变量，分离转化为返回函数各自的变量）
            def g():
                return j * j

            return g

        fs.append(f(i))
        # print(fs)
    return fs


# 5 匿名函数


# 6 装饰器
# 参见：https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)

        # print('haha')
        return wrapper

    return decorator


# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
def base2(x, base=2):
    return int(x, base)


int2 = functools.partial(int, base=2)
max2 = functools.partial(max, 10)


@log('execute')
def now():
    print '2013-12-25'


if __name__ == '__main__':
    pass
    # print str2num()

    # print(num2chen([1, 2, 3, 4]))

    # print(sp_filter(['A', '', 'B', None, 'C', '  ']))

    # print(sort([36, 5, 12, 9, 21]))

    # print(sort_ignore(['bob', 'about', 'Zoo', 'Credit']))

    # func = lazy_sum(1, 2, 3, 7, 7)
    # re = func()
    # print(re)

    # f1, f2, f3 = count()
    # f11, f21, f31 = count1()
    # print(f1(), f2(), f3())
    # print(f11(), f21(), f31())

    # print(now())
    # print(now.__name__)

    print(base2('10010'))
    print(int2('10010'))
    print(max2(4, 5, 6, 9))
