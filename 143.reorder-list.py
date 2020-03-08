"""
143.Reorder List

Difficulty: Medium
Given a singly linked list L: L0&rarr;L1&rarr;&hellip;&rarr;Ln-1&rarr;Ln,
reorder it to: L0&rarr;Ln&rarr;L1&rarr;Ln-1&rarr;L2&rarr;Ln-2&rarr;&hellip;

You may not modify the values in the list&#39;s nodes, only nodes itself may be changed.

Example 1:


Given 1-&gt;2-&gt;3-&gt;4, reorder it to 1-&gt;4-&gt;2-&gt;3.

Example 2:


Given 1-&gt;2-&gt;3-&gt;4-&gt;5, reorder it to 1-&gt;5-&gt;2-&gt;4-&gt;3.



Link: https://leetcode.com/problems/143/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        



import unittest
        
class SolutionCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.solution(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    