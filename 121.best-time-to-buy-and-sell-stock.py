"""
121.Best Time to Buy and Sell Stock

Difficulty: Easy
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:


Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
&nbsp;            Not 7-1 = 6, as selling price needs to be larger than buying price.


Example 2:


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.



Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List
import unittest

class Solution:
    # 64 ms	13.9 MB
    # 62% 86%
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        [min_int, *_] = prices
        max_profit = 0
        for i in prices:
            if i < min_int:
                min_int = i
            else:
                max_profit = max(i - min_int, max_profit)
        return max_profit



class SolutionCase(unittest.TestCase):
    def test_max_profit(self):
        s = Solution()
        for i, o in [
                ([], 0),
                ([7, 1, 5, 3, 6, 4], 5),
                ([7, 6, 4, 3, 1], 0)
        ]:
            self.assertEqual(s.maxProfit(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
