"""
3249.Count the Number of Good Nodes

Difficulty: Medium
There is an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

A node is good if all the subtrees rooted at its children have the same size.

Return the number of good nodes in the given tree.

A subtree of treeName is a tree consisting of a node in treeName and all of its descendants.

 
Example 1:


Input: edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]

Output: 7

Explanation:

All of the nodes of the given tree are good.


Example 2:


Input: edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]

Output: 6

Explanation:

There are 6 good nodes in the given tree. They are colored in the image above.

Example 3:


Input: edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]

Output: 12

Explanation:

All nodes except node 9 are good.



 
Constraints:


	2 <= n <= 105
	edges.length == n - 1
	edges[i].length == 2
	0 <= ai, bi < n
	The input is generated such that edges represents a valid tree.



Link: https://leetcode.com/problems/count-the-number-of-good-nodes/
"""

from typing import DefaultDict, List
import unittest

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        s = {}
        m = {}
        for p, c in edges:
            for k in [p, c]:
                if k not in m:
                    m[k] = {}
            m[p][c] = 1
            m[c][p] = 1
        count = 0
        def get_sum(n):
            nonlocal count
            s[n] = 1
            ls = [c for c in m[n].keys() if c not in s]
            if len(ls):
                flag = True
                last = None
                s[n] = 1
                for c in ls:
                    r = get_sum(c)
                    s[n] += r
                    if not last:
                        last = r
                    elif r != last:
                        flag = False
                if flag:
                    count += 1
                return s[n]
            else:
                count += 1
            return 1
        get_sum(0)
        # print(s)
        return count
    def countGoodNodess(self, edges: List[List[int]]) -> int:
        ans = 0
        adj = DefaultDict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            nonlocal ans
            subtree_sizes = []
            
            for child in adj[node]:
                if child != parent:
                    subtree_size = dfs(child, node)
                    subtree_sizes.append(subtree_size)
            
            if len(set(subtree_sizes)) <= 1:
                ans += 1
            
            return sum(subtree_sizes) + 1
        
        dfs(0, -1)
        return ans
    # def countGoodNodes(self, edges: List[List[int]]) -> int:
    #     s = {}
    #     cm = {}
    #     pm = {}
    #     for p, c in edges:
    #         cm[c] = p
    #         for k in [p, c]:
    #             if k not in pm:
    #                 pm[k] = []
    #             if k not in s:
    #                 s[k] = 0
    #         pm[p] = pm[p] + [c]
    #         cursor = c
    #         while cursor:
    #             s[cursor] += 1
    #             if cursor in cm:
    #                 cursor = cm[cursor]
    #             else:
    #                 cursor = None
    #     count = 0
    #     print(s, cm, pm)
    #     for cs in pm.values():
    #         if len(cs) == 0 or len([c for c in cs if s[c] == s[cs[0]]]) == len(cs):
    #             count = count + 1
    #     return count
                

class SolutionCase(unittest.TestCase):
    def test_count_good_nodes(self):
        s = Solution()
        for i, o in [
                ([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], 7),
                ([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]], 6),
                ([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]], 12),
                ([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]], 6),
                ([[1,0],[3,0],[2,3]], 3)
        ]:
            self.assertEqual(s.countGoodNodes(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
