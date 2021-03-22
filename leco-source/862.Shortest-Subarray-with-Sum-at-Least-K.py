"""
862.Shortest Subarray with Sum at Least K

Difficulty: Hard
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 





Example 1:


Input: A = [1], K = 1
Output: 1



Example 2:


Input: A = [1,2], K = 4
Output: -1



Example 3:


Input: A = [2,-1,2], K = 3
Output: 3


 

Note:


	1 <= A.length <= 50000
	-10 ^ 5 <= A[i] <= 10 ^ 5
	1 <= K <= 10 ^ 9






Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""

from typing import List
import collections

# 滑动窗口
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        length = len(A)
        res = length + 1
        sum_slice = 0
        sum_slice_arr = collections.deque([(-1, 0)])
        for idx, val in enumerate(A):
            sum_slice += val
            if val > 0:
                while sum_slice_arr and sum_slice - sum_slice_arr[0][1] >= K:
                    res = min(res, idx - sum_slice_arr.popleft()[0])
            else:
                while sum_slice_arr and sum_slice <= sum_slice_arr[-1][1]:
                    sum_slice_arr.pop()
            sum_slice_arr.append((idx, sum_slice))
        return res if res <= length else -1


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().shortestSubarray
        self.assertEqual(func([1,2], 4), -1)
        self.assertEqual(func([1], 1), 1)
        self.assertEqual(func([2, -1, 2], 3), 3)
        self.assertEqual(func([48,99,37,4,-31], 140), 2)
        self.assertEqual(func([77,19,35,10,-14], 19), 1)

if __name__ == "__main__":
    unittest.main()
