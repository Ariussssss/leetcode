# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-26 23:45:18


"""
输入一个字符串
如果AAA变成AA
如果AABB变成AAB
"""

REGEX = {
    'AAA': 'AA',
    'AABB': 'AAB'
}
def filter_str(req_str):
    req_str = list(req_str)
    length = len(req_str)
    print()
    for idx in range(0, length - 2):
        first = ''.join(req_str[idx: idx + 4]) == 'AABB'
        sec = ''.join(req_str[idx: idx + 3]) == 'AAA'
        if first or sec:
            req_str.pop(idx + 2)
            return filter_str(req_str)
    return ''.join(req_str)


import unittest

class TestSolution(unittest.TestCase):
    def test_filter_str(self):
        fn = filter_str
        self.assertEqual(fn('AAAA'), 'AA')
        self.assertEqual(fn('AAABB'), 'AAB')
        self.assertEqual(fn('AAABBABABAABAAABAAAABBABB'), 'AABABABAABAABAABABB')

if __name__ == '__main__':
    unittest.main()
