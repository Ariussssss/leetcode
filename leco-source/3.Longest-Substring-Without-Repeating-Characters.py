"""
3.Longest Substring Without Repeating Characters

Difficulty: Medium
Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Example 4:


Input: s = ""
Output: 0


 
Constraints:


	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.



Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import List
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        key_map = {}
        max_count, start, end = 0, 0, 0
        while end < len(s):
            new_max_count = end - start
            if s[end] in key_map and key_map[s[end]] >= start:
                start = key_map[s[end]] + 1
                max_count = max(new_max_count, max_count)
            elif (end + 1 == len(s)):
                max_count = max(new_max_count + 1, max_count)
            key_map[s[end]], end = end, end + 1
        return max_count

    # slice mode
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        first, cur = 0, 1
        ans = -1
        while cur < len(s):
            temp = s[first: cur]
            if s[cur] in temp:
                first += temp.index(s[cur]) + 1
            cur += 1
            ans = max(ans, cur - first)
        return ans
    
class lengthOfLongestSubstringCase(unittest.TestCase):
    def test_three_sum(self):
        s = Solution()
        for i, o in [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), (" ", 1), ("aab", 2), ("tmmzuxt", 5), ("abcabcbb", 3)]:
            self.assertEqual(s.lengthOfLongestSubstring(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
