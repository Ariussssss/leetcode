"""
82.Remove Duplicates from Sorted List II

Difficulty: Medium
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:


Input: 1-&gt;2-&gt;3-&gt;3-&gt;4-&gt;4-&gt;5
Output: 1-&gt;2-&gt;5


Example 2:


Input: 1-&gt;1-&gt;1-&gt;2-&gt;3
Output: 2-&gt;3



Link: https://leetcode.com/problems/82/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        



import unittest
        
class SolutionCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.solution(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    