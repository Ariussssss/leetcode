"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


"""

import unittest
from typing import List

# 斐波那契数列（Fibonacci sequence）

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            sum_list = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                sum_list.append(max(sum_list[i-1], nums[i] + sum_list[i-2]))
            return sum_list.pop()
        return sum(nums)
        
class HouseRobberCase(unittest.TestCase):
    def test_house_robber(self):
        s = Solution()
        for i, o in [
                # ([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211], None),
                ([1,100,3, 1, 100], 200),
                ([1,2,3, 1], 4),
                ([2, 7, 9, 3, 1], 12)]:
            self.assertEqual(s.rob(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()

