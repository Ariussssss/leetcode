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

from typing import List
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Hard code first
    # 108 ms	22.2 MB
    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        record = []
        tmp = []
        while cur:
            record.append(cur)
            cur = cur.next
        idx = 0
        length = len(record)
        while idx < length / 2:
            tmp.append(record[idx])
            if idx * 2 < length:
                tmp.append(record[length - idx - 1])
            idx += 1
        for idx, cur in enumerate(tmp):
            cur.next = tmp[idx+1] if idx < length - 1 else None

    # 88 ms	22.1 MB
    # 90% 7%
    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        tmp = []
        while cur:
            tmp.append(cur)
            cur = cur.next
        length = len(tmp)
        mid = length // 2
        for idx, cur in enumerate(tmp):
            if idx > mid:
                cur.next = tmp[length - idx]
            elif idx < mid:
                cur.next = tmp[length - 1 - idx]
            else:
                cur.next = None
        
        # Fixme
        # half interation

    # 108 ms	35.5 MB
    # 18% 7%
    def reorderList(self, head: ListNode) -> None:
        cur = head
        tmp = []
        while cur:
            tmp.append(cur)
            cur = cur.next
        length = len(tmp)
        if length < 2:
            return
        def sub(node: ListNode, idx) -> None:
            if idx >= length // 2:
                node.next = None
            else:
                next_node = node.next
                node.next, tmp[length - 1 - idx].next = tmp[length - 1 - idx], next_node
                sub(next_node, idx + 1)
        sub(tmp[0], 0)

# Comment:
# Expected to be fast with more memory used.
# But while slower?


class SolutionCase(unittest.TestCase):
    def build_node_list(self, arr: List[int]) -> ListNode:
        parent = ListNode(None)
        cur = parent
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return parent.next

    def print_list(self, head: ListNode) -> str:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
        return self.fmt(res)

    def fmt(self, arr: List[int]) -> str:
        return ",".join([str(i) for i in arr])

    def test_reorder_list(self):
        s = Solution()
        for i, o in [
                ([1,2,3,4], [1,4,2,3]),
                ([1,2,3,4,5], [1,5,2,4,3]),
        ]:
            head = self.build_node_list(i)
            s.reorderList(head)
            
            self.assertEqual(self.print_list(head), self.fmt(o))


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
