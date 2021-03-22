"""
1.Two Sum

Difficulty: Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:


Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:


Input: nums = [3,3], target = 6
Output: [0,1]


 
Constraints:


	2 <= nums.length <= 103
	-109 <= nums[i] <= 109
	-109 <= target <= 109
	Only one valid answer exists.



Link: https://leetcode.com/problems/two-sum/
"""

from typing import List
import unittest

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, num in enumerate(nums):
            rest = target - num
            if rest in d:
                return [d[rest], idx]
            else:
                d[num] = idx

    def twoSumInSort(self, nums, target):
        # two-pointer
        def twoSum1(self, numbers, target):
            l, r = 0, len(numbers)-1
            while l < r:
                s = numbers[l] + numbers[r]
                if s == target:
                    return [l+1, r+1]
                elif s < target:
                    l += 1
                else:
                    r -= 1
         
        # dictionary           
        def twoSum2(self, numbers, target):
            dic = {}
            for i, num in enumerate(numbers):
                if target-num in dic:
                    return [dic[target-num]+1, i+1]
                dic[num] = i
         
        # binary search        
        def twoSum(self, numbers, target):
            for i in xrange(len(numbers)):
                l, r = i+1, len(numbers)-1
                tmp = target - numbers[i]
                while l <= r:
                    mid = l + (r-l)//2
                    if numbers[mid] == tmp:
                        return [i+1, mid+1]
                    elif numbers[mid] < tmp:
                        l = mid+1
                    else:
                        r = mid-1


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().twoSum
        self.assertEqual(func([3, 3], 6), [0, 1])
        self.assertEqual(func([3, 2, 4], 6), [1, 2])
        self.assertEqual(func([2, 7, 11, 15], 9), [0, 1])

if __name__ == "__main__":
    unittest.main()
