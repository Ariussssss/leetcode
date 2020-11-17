# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-28 18:01:11

"""
1020-Partition-Array-Into-Three-Parts-With-Equal-Sum
Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""

class Solution:
    @staticmethod
    def partSum(arr):
        sum_dict = {}
        def getData(x, y):
            key = '{0}:{1}'.format(x, y)
            if key not in sum_dict:
                sum_dict[key] = sum(arr[x:y])
            return sum(arr[x:y])
        length = len(arr)
        left = 0
        while left < length:
            right = length
            while right >= left:
                ll, ml, rl = getData(0, left), getData(left, right),\
                    getData(right, length)
                if ll == ml and ml == rl:
                    return True
                right -= 1
            left += 1
        return False

    @staticmethod
    def canPartSum(arr):
        s = sum(arr)
        if s % 3 == 0:
            s /= 3
            targets = [2 * s, s]
            res = 0
            for a in arr:
                res += a
                if res == targets[-1]:
                    targets.pop()
                if not targets:
                    return True
        return False

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().canPartSum
        self.assertEqual(func([1, 1, 1]), True)
        self.assertEqual(func([0,2,1,-6,6,7,9,-1,2,0,1]), False)
        self.assertEqual(func([0,2,1,-6,6,-7,9,1,2,0,1]), True)
        self.assertEqual(func([0,2,1,-6,6,7,9,-1,2,0,1]), False)


if __name__ == "__main__":
    unittest.main()