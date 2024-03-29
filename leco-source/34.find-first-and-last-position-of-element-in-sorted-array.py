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
    def first_occurance(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                if mid-1>=0 and nums[mid-1]==target:
                    high = mid-1
                else:
                    return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low = mid+1
        return -1
    
    def last_occurance(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                if mid+1<len(nums) and nums[mid+1]==target:
                    low = mid+1
                else:
                    return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low = mid+1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        return [self.first_occurance(nums,target),self.last_occurance(nums,target)]

class SolutionCase(unittest.TestCase):
    def test_search_range(self):
        s = Solution()
        for i, o in [
            ([[[1, 2, 3], 1], [0, 0]]),
            ([[[1, 2], 2], [1, 1]]),
            ([[[2, 2], 2], [0, 1]]),
            ([[[1], 1], [0, 0]]),
            ([[5, 7, 7, 8, 8, 10], 8], [3, 4]),
            ([[5, 7, 7, 8, 8, 10], 6], [-1, -1]),
        ]:
            self.assertEqual(s.searchRange(*i), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
