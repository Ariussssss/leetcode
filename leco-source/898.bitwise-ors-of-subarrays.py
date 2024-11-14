"""
898.Bitwise ORs of Subarrays

Difficulty: Medium
We have an array arr of non-negative integers.

For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

Return the number of possible results. Results that occur more than once are only counted once in the final answer

 
Example 1:


Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.


Example 2:


Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.


Example 3:


Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.


 
Constraints:


	1 <= nums.length <= 5 * 104
	0 <= nums[i] <= 109



Link: https://leetcode.com/problems/bitwise-ors-of-subarrays/
"""

from typing import List
import unittest

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur, res=set(),set()
        print('1', cur, res)
        for i in A:
            print('i:', i, cur, res)
            cur={i|j for j in cur} |{i}
            print(cur)
            res|=cur
            print(res)
        return len(res)

class SolutionCase(unittest.TestCase):
    def test_subarray_bitwise_o_rs(self):
        s = Solution()
        for i, o in [([0], 1), ([1,1,2], 3), ([1,2,4], 6), ([1,2,1,3,4], 5)]:
            self.assertEqual(s.subarrayBitwiseORs(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    