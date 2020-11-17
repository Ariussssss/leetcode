"""
动态规划
有1，4，6，16面值
价格N
用最少m个
"""

def charge(n, money=(1,4,6,16)):
    if n in money:
        return 1
    else:
        if (n % money[3]) == 0:
            return n / money[3]
        return min([
            charge(n - x)
            for x in money
            if (n - x) > 0
        ]) + 1

res = [0]
def charge1(n, money=(1,4,6,16)):
    while len(res) <= n:
        m = len(res)
        res.append(min([
            res[m - x]
            for x in money
            if m >= x
        ]) + 1)
    return res[n]

import unittest

class TestSolution(unittest.TestCase):
    def test_filter_str(self):
        fn = charge1
        self.assertEqual(fn(9), 3)
        self.assertEqual(fn(8), 2)
        self.assertEqual(fn(16), 1)
        self.assertEqual(fn(17), 2)
        self.assertEqual(fn(23), 3)
        self.assertEqual(fn(64), 4)
        self.assertEqual(fn(65), 5)
        self.assertEqual(fn(68), 5)
        self.assertEqual(fn(1024), 64)

if __name__ == '__main__':
    unittest.main()
