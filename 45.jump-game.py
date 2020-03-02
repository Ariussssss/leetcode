# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-29 20:17:41


"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
class Solution:
    def jump(self, nums) -> int:
        target = len(nums) - 1
        maps = {}
        maps[0] = 0
        checked = set()
        reach = [0]
        while target not in maps.keys():
            idx = reach.pop(0)
            for x in range(1, nums[idx] + 1):
                nidx = x + idx
                if (nidx) in maps.keys():
                    maps[nidx] = min([maps[nidx], maps[idx] + 1])
                else:
                    maps[nidx] = maps[idx] + 1
                    reach.append(nidx)
        return maps[target]

    def jump1(self, nums) -> int:
        target = len(nums) - 1
        x = 0
        jump_count = 0
        if target == 0:
            return 0
        while x + nums[x] < target:
            max_idx = x
            max_num = x + nums[x]
            for idx in range(1, nums[x] + 1):
                new_max_idx = x + idx
                new_max_num = new_max_idx + nums[new_max_idx]
                if max_num < new_max_num:
                    max_idx, max_num = new_max_idx, new_max_num
            x = max_idx
            jump_count += 1
        return jump_count + 1
    
# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().jump1
        self.assertEqual(func([2,3,1,1,4]), 2)
        self.assertEqual(func([2,3,0,1,4]), 2)
        self.assertEqual(func([0]), 0)

if __name__ == "__main__":
    unittest.main()
