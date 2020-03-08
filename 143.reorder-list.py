"""
143.Reorder List

Difficulty: Medium
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list&#39;s nodes, only nodes itself may be changed.

Example 1:


Given 1→2→3→4, reorder it to 1→4→2→3.

Example 2:


Given 1→2→3→4→5, reorder it to 1→5→2→4→3.



Link: https://leetcode.com/problems/reorder-list/
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
    def test_reorder_list(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.reorderList(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    