# coding=utf-8
from __future__ import unicode_literals, division

# 测试新版本的特性

if __name__ == '__main__':
    print
    '\'xxx\' is unicode?', isinstance('xxx', unicode)
    print
    'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
    print
    '\'xxx\' is str?', isinstance('xxx', str)
    print
    'b\'xxx\' is str?', isinstance(b'xxx', str)

    print
    print
    '10 / 3 =', 10 / 3
    print
    '10.0 / 3 =', 10.0 / 3
    print
    '10 // 3 =', 10 // 3
