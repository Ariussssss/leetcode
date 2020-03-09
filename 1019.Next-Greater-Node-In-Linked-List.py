"""
1019-Next-Greater-Node-In-Linked-List
1019. Next Greater Node In Linked List
User Accepted: 1614
User Tried: 1982
Total Accepted: 1651
Total Submissions: 3261
Difficulty: Medium
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
"""

# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        now = head
        queue = []
        while now:
            queue.append(now.val)
            now = now.next
        res = [0 for x in range(len(queue))]
        stack = []
        for x in range(len(queue)-1, -1, -1):
            while stack and queue[x] >= queue[stack[-1]]:
                stack.pop()
            if stack:
                res[x] = queue[stack[-1]]
            stack.append(x)
        return res



# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        # 976769
        func = Solution().nextLargerNodes
        head = ListNode(9)
        head.next = ListNode(7)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(7)
        head.next.next.next.next = ListNode(6)
        head.next.next.next.next.next = ListNode(9)
        self.assertEqual(func(head), [0,9,7,9,9,0])

if __name__ == "__main__":
    unittest.main()