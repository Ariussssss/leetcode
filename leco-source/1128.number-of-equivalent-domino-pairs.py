"""
1128.Number of Equivalent Domino Pairs

Difficulty: Easy
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
Example 1:


Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Example 2:


Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3


 
Constraints:


	1 <= dominoes.length <= 4 * 104
	dominoes[i].length == 2
	1 <= dominoes[i][j] <= 9



Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""

from typing import List
import unittest

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = {}
        m = {}
        for d in dominoes:
            i, j = d
            key = f"{j}-{i}" if i > j else f"{i}-{j}"
            if key not in c:
                c[key] = 1
                m[key] = 0
            else:
                m[key] += c[key]
                c[key] += 1
        return sum(m.values())


class SolutionCase(unittest.TestCase):
    def test_num_equiv_domino_pairs(self):
        s = Solution()
        for i, o in [
                ([[1,2],[2,1],[3,4],[5,6]], 1),
                ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),
                ([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]], 15)
        ]:
            self.assertEqual(s.numEquivDominoPairs(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    
