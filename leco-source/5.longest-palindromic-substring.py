"""
5.Longest Palindromic Substring

Difficulty: Medium
Given a string s, return the longest palindromic substring in s.

 
Example 1:


Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:


Input: s = "cbbd"
Output: "bb"


 
Constraints:


	1 <= s.length <= 1000
	s consist of only digits and English letters.



Link: https://leetcode.com/problems/longest-palindromic-substring/
"""

from typing import List
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        substr: any = ''
        for i in range(len(s)):
            j = k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            odd = s[j + 1:k]
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            even = s[j + 1:k]
            print(odd, even, substr)
            substr = max(substr, odd, even, key=len)

        return substr


class SolutionCase(unittest.TestCase):
    def test_longest_palindrome(self):
        s = Solution()
        for i, o in [("cbbd", "bb"), ("babad", "bab")]:
            self.assertEqual(s.longestPalindrome(i), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
