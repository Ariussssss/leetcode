"""
70.Climbing Stairs

Difficulty: Easy
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:


Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:


Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


 
Constraints:


	1 <= n <= 45



Link: https://leetcode.com/problems/climbing-stairs/
"""

from typing import List
import unittest

class Solution:
    # 56 ms 6%	14.2 MB 42%
    res_map = {}
    def climbStairs(self, n: int) -> int:
        if str(n) in self.res_map:
            return self.res_map[str(n)]
        if n < 2:
            return 1
        if n == 2:
            return 2
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.res_map[str(n)] = res
        return res
        
class SolutionCase(unittest.TestCase):
    def test_climb_stairs(self):
        s = Solution()
        for i, o in [(2, 2), (3, 3)]:
            self.assertEqual(s.climbStairs(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
