"""
102.Binary Tree Level Order Traversal

Difficulty: Medium
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]



Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from typing import List
import unittest
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 96ms 6%
    # 12m 100%
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        res, tmp = [], []
        targets = [[root], []]
        while len(targets[0]) > 0:
            cur = targets[0].pop(0)
            if cur != None:
                if cur.val != None:
                    tmp.append(cur.val)
                targets[1].append(cur.left)
                targets[1].append(cur.right)
            if not targets[0]:
                if tmp:
                    res.append(tmp)
                    tmp = []
                targets = [targets[1], targets[0]]
        return res

    # 32ms 73%
    # 13m 875
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self._levels = []
        self.get_level(root, 0)
        return self._levels

    def get_level(self, root, depth):
        if not root:
            return
        if depth == len(self._levels):
            self._levels.append([])
        if root.val != None:
            self._levels[depth].append(root.val)
        self.get_level(root.left, depth + 1)
        self.get_level(root.right, depth + 1)


# comment:
# Use BFS.
# Iteration way requires more cache and codes to handle it.
# Recursion way can be easier to read and less code for cached.


class SolutionCase(unittest.TestCase):
    def buildTree(self, arr: List, idx: int = 0) -> TreeNode:
        if idx >= len(arr):
            return None
        root = TreeNode(arr[idx])
        root.left = self.buildTree(arr, 2 * idx + 1)
        root.right = self.buildTree(arr, 2 * idx + 2)
        return root

    def test_level_order(self):
        s = Solution()
        for i, o in [
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1, 2], [[1], [2]]),
            ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3, 4], [5]]),
            (
                [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8],
                [[0], [2, 4], [1, 3, -1], [5, 1, 6, 8]],
            ),
        ]:
            self.assertEqual(s.levelOrder(self.buildTree(i)), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
