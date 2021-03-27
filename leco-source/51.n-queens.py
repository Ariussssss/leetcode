"""
51.N-Queens

Difficulty: Hard
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 
Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


Example 2:


Input: n = 1
Output: [["Q"]]


 
Constraints:


	1 <= n <= 9



Link: https://leetcode.com/problems/n-queens/
"""

from typing import List
import collections
import unittest


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ban_row = [False] * n
        self.ban_right_down = collections.defaultdict(bool)
        self.ban_left_down = collections.defaultdict(bool)
        self.cur_board = [["."] * n for _ in range(n)]
        self.sols = []

        def get_format(board):
            return ["".join(line) for line in board]

        def dfs(y, mark):
            if mark == n:
                self.sols.append(get_format(self.cur_board))
            elif y >= n:
                return
            else:
                for x in range(n):
                    if not (
                            self.ban_row[x]
                            or self.ban_right_down[x - y]
                            or self.ban_left_down[x + y]
                    ):
                        self.ban_row[x] = self.ban_right_down[
                            x - y
                        ] = self.ban_left_down[
                            x + y
                        ] = True
                        self.cur_board[y][x] = "Q"
                        dfs(y + 1, mark + 1)
                        self.ban_row[x] = self.ban_right_down[
                            x - y
                        ] = self.ban_left_down[
                            x + y
                        ] = False
                        self.cur_board[y][x] = "."

        dfs(0, 0)
        return self.sols

class SolutionCase(unittest.TestCase):
    def test_solve_n_queens(self):
        s = Solution()
        for i, o in [
            (1, [["Q"]]),
            (
                4,
                [
                    [".Q..", "...Q", "Q...", "..Q."],
                    ["..Q.", "Q...", "...Q", ".Q.."],
                ],
            ),
        ]:
            self.assertEqual(s.solveNQueens(i), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
