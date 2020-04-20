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
    # 40 ms	13.2 MB
    # 65% 86%
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left = mid+1
        return -1
    # 32 ms	13.2 MB
    # 96.84% 86%
    def search1(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


class SolutionCase(unittest.TestCase):
    def test_search(self):
        s = Solution()
        for i, o in [
                (([4,5,6,7,0,1,2], 0), 4),
                (([4,5,6,7,0,1,2], 3), -1)
        ]:
            self.assertEqual(s.search(*i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
