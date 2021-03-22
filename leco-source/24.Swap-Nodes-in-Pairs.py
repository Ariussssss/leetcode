"""
24.Swap Nodes in Pairs

Difficulty: Medium
Given a linked list, swap every two adjacent nodes and return its head.

 
Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]


Example 2:


Input: head = []
Output: []


Example 3:


Input: head = [1]
Output: [1]


 
Constraints:


	The number of nodes in the list is in the range [0, 100].
	0 <= Node.val <= 100


 
Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)

Link: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from typing import List
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        next_header = head
        if head and head.next:
            next_header, head.next.next, head.next = head.next, head, self.swapPairs(head.next.next)
        return next_header

class SwapNodesInPairsCase(unittest.TestCase):
    def create_list(self, arr: List[int]):
        if len(arr) == 0:
            return None
        pre_head = ListNode(None)
        target = pre_head
        for i in arr:
            target.next = ListNode(i)
            target = target.next
        return pre_head.next

    def print_nodes(self, head: ListNode):
        res = []
        target = head
        while target:
            res.append(target.val)
            target = target.next
        return ",".join([str(e) for e in res])
            
    def test_swap_nodes_in_pairs(self):
        s = Solution()
        for i, o in [([1,2,3,4], [2,1,4,3])]:
            self.assertEqual(self.print_nodes(s.swapPairs(self.create_list(i))),  self.print_nodes(self.create_list(o)))


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    # s = SwapNodesInPairsCase()
    # a = s.create_list([2,1,4,3])
    # print(s.print_nodes(a))

