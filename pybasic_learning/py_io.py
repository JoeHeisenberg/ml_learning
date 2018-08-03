# coding=utf-8

"""
this module is for bugs and exception test
"""

__author__ = 'joe'

if __name__ == '__main__':
    pass
    # f = open('notes', 'r')
    # print(f.read())
    # f.close()

    with open('notes', 'r') as f:
        # print(f.read())
        for line in f.readlines():
            print(line.strip())

    with open('notes', 'w') as w:
        w.writelines('i am writing !!')
