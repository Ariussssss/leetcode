"""
1017. Convert to Base -2
User Accepted: 1189
User Tried: 1451
Total Accepted: 1249
Total Submissions: 2618
Difficulty: Medium
Given a number N, return a string consisting of "0"s and "1"s that represents
 its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
 

Note:

0 <= N <= 10^9
"""
# TEST ONLY
import unittest


class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"

        b = N
        arr = []
        while b != 0:
            c = b % -2
            if c < 0:
                c = 1
                b = (b - c) // -2
            else:
                b = b // -2
            arr.append(str(c))
        arr.reverse()
        return "".join(arr)


class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().baseNeg2
        self.assertEqual(func(2), "110")
        self.assertEqual(func(3), "111")
        self.assertEqual(func(4), "100")
        self.assertEqual(func(6), "11010")
        self.assertEqual(func(16), "10000")


if __name__ == "__main__":
    unittest.main()
