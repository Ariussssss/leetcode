"""
4.Median of Two Sorted Arrays

Difficulty: Hard
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2&nbsp;cannot be both empty.

Example 1:


nums1 = [1, 3]
nums2 = [2]

The median is 2.0


Example 2:


nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5



Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List
import unittest


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sub = []
        total_length = len(nums1) + len(nums2)
        while len(sub) < total_length:
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] > nums2[0]:
                    sub.append(nums2.pop(0))
                else:
                    sub.append(nums1.pop(0))
            elif len(nums1) > 0:
                sub.append(nums1.pop(0))
            else:
                sub.append(nums2.pop(0))

            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[-1] < nums2[-1]:
                    sub.append(nums2.pop())
                else:
                    sub.append(nums1.pop())
            elif len(nums1) > 0:
                sub.append(nums1.pop())
            elif len(nums2) > 0:
                sub.append(nums2.pop())
        if total_length % 2 == 0:
            return (sub[-2] + sub[-1]) / 2
        else:
            return sub[-1]
        
class SolutionCase(unittest.TestCase):
    def test_find_median_sorted_arrays(self):
        s = Solution()
        for i, o in [[[[1, 3], [2]], 2.0], [[[1, 2], [3, 4]], 2.5]]:
            self.assertEqual(s.findMedianSortedArrays(*i), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
