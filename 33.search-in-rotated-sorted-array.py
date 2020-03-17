"""
33.Search in Rotated Sorted Array

Difficulty: Medium
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm&#39;s runtime complexity must be in the order of&nbsp;O(log&nbsp;n).

Example 1:


Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


Example 2:


Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


class SolutionCase(unittest.TestCase):
    def test_search(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.search(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    