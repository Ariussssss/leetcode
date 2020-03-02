'''
1022-Smallest-Integer-Divisible-by-K]

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

 

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:

1 <= K <= 10^5

'''

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        res = 1
        if K % 10 not in [1,3,7,9]:
            return -1
        checked = set()
        while res % K != 0:
            res = (res * 10 + 1) % K
            if len(checked) + 1 > K:
                return -1
            if res in checked:
                return -1
            checked.add(res)
        return len(checked) + 1


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().smallestRepunitDivByK
        self.assertEqual(func(1), 1)
        self.assertEqual(func(2), -1)
        self.assertEqual(func(3), 3)
        self.assertEqual(func(49991), 4999)


if __name__ == "__main__":
    unittest.main()