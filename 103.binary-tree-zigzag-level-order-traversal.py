"""
103.Binary Tree Zigzag Level Order Traversal

Difficulty: Medium
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]



Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        



import unittest

class SolutionCase(unittest.TestCase):
    def test_reorder_list(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.reorderList(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    