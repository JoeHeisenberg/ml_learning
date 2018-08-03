# coding=utf-8

"""
this module is for bugs and exception test
"""

__author__ = 'joe'

if __name__ == '__main__':
    pass
    try:
        print 'try...'
        r = 10 / int('a')
        print 'result:', r
    except ValueError, e:
        print 'ValueError:', e
    except ZeroDivisionError, e:
        print 'ZeroDivisionError:', e
    else:
        print 'no error!'
    finally:
        print 'finally...'
    print 'END'
