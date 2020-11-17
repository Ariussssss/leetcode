"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

"""

import unittest
from typing import List
from functools import cmp_to_key

class Solution:
    def cmp(x, y):
        if x == y:
            return 0
        elif x + y > y + x:
            return 1
        return -1

    def largestNumber(self, nums):
        return str(int("".join(sorted([str(x) for x in nums], 
                                      key=cmp_to_key(Solution.cmp), reverse=True))))
    def largestNumber2(self, nums):
        return str(int("".join(sorted([str(x) for x in nums], 
                        cmp = lambda a, b: int(b + a) - int(a + b)))))

class LargestNumberCase(unittest.TestCase):
    def test_largest_number(self):
        s = Solution()
        for i, o in [([10,2], "210"),
                     ([3,30,34,5,9], "9534330"),
                     ([0, 0], "0"),
                     ([1], "1"),
                     ([12,121], "12121")]:
            self.assertEqual(s.largestNumber(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
