"""
560.Subarray Sum Equals K

Difficulty: Medium
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

 
Constraints:


	1 <= nums.length <= 2 * 104
	-1000 <= nums[i] <= 1000
	-107 <= k <= 107



Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""

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
