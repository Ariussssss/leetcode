"""
103.Binary Tree Zigzag Level Order Traversal

Difficulty: Medium
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]


Example 2:


Input: root = [1]
Output: [[1]]


Example 3:


Input: root = []
Output: []


 
Constraints:


	The number of nodes in the tree is in the range [0, 2000].
	-100 <= Node.val <= 100



Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

from typing import List
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self._levels = []
        self.get_level(root, 0)
        return self._levels

    def get_level(self, root, depth):
        if not root:
            return
        if depth == len(self._levels):
            self._levels.append([])
        if root.val != None:
            if (depth % 2 == 0):
                self._levels[depth].append(root.val)
            else:
                self._levels[depth].insert(0, root.val)
        self.get_level(root.left, depth + 1)
        self.get_level(root.right, depth + 1)


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
            ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
            ([1, 2], [[1], [2]]),
            ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3, 4], [5]]),
            (
                [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8],
                [[0], [4, 2], [1, 3, -1], [8, 6, 1, 5]],
            ),
        ]:
            self.assertEqual(s.zigzagLevelOrder(self.buildTree(i)), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
