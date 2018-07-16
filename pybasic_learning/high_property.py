# coding=utf-8
# this is a test for python high properties

# 1 切片
import os
import pyoop_basic as op

L = range(50)


# au = op.__author__

# 2 迭代
def ite():
    for key in Map.iterkeys():
        print key

    for value in Map.itervalues():
        print(value)

    for it in Map.iteritems():
        print it

    for k, v in Map.iteritems():
        print k, '=', v

    # 同时引用了两个变量
    for i, value in enumerate(['A', 'B', 'C']):
        print i, value


# 列表生成式 list comprehension
def lscom():
    L0 = range(1, 11, 2)
    # x * x位置实现对循环过程中变量的操作
    L1 = [x * x for x in range(1, 11)]
    L2 = [x * x for x in range(1, 11) if x % 2 == 0]  # 带过滤条件

    L3 = [m + n for m in 'ABC' for n in 'XYZ']  # 使用多层循环

    Ldir_name = [d for d in os.listdir('.')]

    print L0, L1, L2
    print L3
    print Ldir_name


# 生成器 Generator 一边循环一边计算的机制
# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
def genera():
    G0 = (x * x for x in range(10))

    print(G0)
    # 通过迭代取出元素
    for n in G0:
        print(n)
        # print(G0)


# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。(调用一次执行一次)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    M = [1, 2, 2, 3, 56, 78, 6]
    Map = {1: 'dbsajh', 20: 'xix', 50: True, 4: 'haha'}

    # print(M)

    # ite()

    # lscom()

    # genera()

    # for n in fib(12):
    #     print n

    # 绕过私有权限控制访问变量
    # st = op.Student('xixi', 16, 'female',66)
    # print(st._Student__name)
    # print(st._score)
