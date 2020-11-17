# https://leetcode.com/problems/subarray-sum-equals-k/

'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2
Note:
    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

from typing import List

class Solution:
    
    def sup(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        elif nums[0] == k:
            return 1 + self.sup(nums[1:], k - nums[0])
        else:
            return self.sup(nums[1:], k - nums[0])

    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        for idx, x in enumerate(nums):
            s = 0
            res += self.sup(nums[idx:], k)
        return res

import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().subarraySum
        self.assertEqual(func([1, 1, 1], 2), 2)
        self.assertEqual(func([1, 2, 3], 3), 2)
        self.assertEqual(func([100, 1, 2, 3, 4], 6), 1)
        self.assertEqual(func([0, 0, 0, 0, 0, 0, 0, 0,
            0, 0], 0), 55)

if __name__ == "__main__":
    unittest.main()