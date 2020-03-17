"""
53.Maximum Subarray

Difficulty: Easy
Given an integer array nums, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.

Example:


Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation:&nbsp;[4,-1,2,1] has the largest sum = 6.


Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


Link: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List
import unittest

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        


class SolutionCase(unittest.TestCase):
    def test_max_sub_array(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.maxSubArray(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    