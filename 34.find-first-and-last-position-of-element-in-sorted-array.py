"""
34.Find First and Last Position of Element in Sorted Array

Difficulty: Medium
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm&#39;s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:


Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import List
import unittest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        flag = False
        while left < right and not flag:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                flag = True
                left = right = mid
        if not flag:
            return [-1, -1]
        left_end  = right_end = mid
        
                


class SolutionCase(unittest.TestCase):
    def test_search_range(self):
        s = Solution()
        for i, o in [
                ([[5,7,7,8,8,10], 8], [3,4])
                ([[5,7,7,8,8,10], 6], [-1,-1])
        ]:
            self.assertEqual(s.searchRange(*i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
