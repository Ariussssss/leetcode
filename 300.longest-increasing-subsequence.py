"""
300.Longest Increasing Subsequence

Difficulty: Medium
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:


Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note: 


	There may be more than one LIS combination, it is only necessary for you to return the length.
	Your algorithm should run in O(n2) complexity.


Follow up: Could you improve it to O(n log n) time complexity?


Link: https://leetcode.com/problems/longest-increasing-subsequence/
"""

from typing import List
import unittest

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        


class SolutionCase(unittest.TestCase):
    def test_length_of_l_i_s(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.lengthOfLIS(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    