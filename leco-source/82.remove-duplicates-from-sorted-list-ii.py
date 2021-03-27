"""
82.Remove Duplicates from Sorted List II

Difficulty: Medium
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:


Input: 1→2→3→3→4→4→5
Output: 1→2→5


Example 2:


Input: 1→1→1→2→3
Output: 2→3



Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = ListNode(0)
        start.next = head
        cur = head
        last = start
        is_duplicate = False
        while cur:
            if not cur.next or cur.next.val != cur.val:
                if is_duplicate:
                    last.next = cur.next
                    is_duplicate = False
                else:
                    last = cur
            else:
                is_duplicate = True
            cur = cur.next
        return start.next


import unittest


class SolutionCase(unittest.TestCase):
    def test_reorder_list(self):
        s = Solution()

        def create_list_node(arr: List[int]):
            head = ListNode(0)
            cur = head
            for i in arr:
                cur.next = ListNode(i)
                cur = cur.next
            return head.next

        def get_list_node_sum(head: ListNode):
            res = 0
            resArr = []
            cur = ListNode(0)
            cur.next = head
            while cur.next:
                res += cur.next.val
                resArr.append(cur.next.val)
                cur = cur.next
            print(resArr)
            return res

        for i, o in [
            (create_list_node([1, 1]), 0),
            (create_list_node([1, 2, 3, 3, 4, 4, 5]), 8),
            (create_list_node([1, 1, 1, 2, 3]), 5),
        ]:
            self.assertEqual(get_list_node_sum(s.deleteDuplicates(i)), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
