"""
1020. Number of Enclaves
User Accepted: 1368
User Tried: 1599
Total Accepted: 1398
Total Submissions: 2693
Difficulty: Medium
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""

from typing import List

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def create_key(arr):
            return ':'.join([str(x) for x in arr])

        def get_around(location: List[int]):
            y, x = location
            up, down = (y - 1, x), (y + 1, x)
            left, right = (y , x - 1), (y, x + 1)
            return up, down, left, right

        def check(location: List[int], can_reach_maps: set,\
                x_length: int, y_length: int)->bool:
            y, x = location
            if y in [0, y_length - 1] or x in [0, x_length - 1]:
                can_reach_maps.add(create_key((y, x)))
                return False
            else:
                up, down, left, right = get_around(location)
                for around in [up, down, left, right]:
                    around_str = create_key(around)
                    if around_str in can_reach_maps:
                        can_reach_maps.add(create_key((y, x)))
                        return False
                return True

        if len(A) == 0 or len(A[0]) == 0:
            return 0
        can_reach_maps = set()
        x_length, y_length = len(A[0]), len(A)
        land_maps = {}
        sum_land = 0
        for y_idx, line in enumerate(A):
            for x_idx, x in enumerate(line):
                if x == 1:
                    now = create_key((y_idx, x_idx))
                    if check((y_idx, x_idx), can_reach_maps, x_length, y_length):
                        sum_land += 1
                        for loc in get_around((y_idx, x_idx)):
                            key = create_key(loc)
                            if key in land_maps.keys():
                                land_maps[key].append(now)
                            else:
                                land_maps[key] = [now]
                    else:
                        now_list = [now]
                        while len(now_list) > 0:
                            now_item = now_list.pop()
                            if now_item in land_maps.keys():
                                now_list += land_maps[now_item]
                                del land_maps[now_item]
                            if now_item not in can_reach_maps:
                                can_reach_maps.add(now_item)
                                sum_land -= 1
        return sum_land

    def numEnclaves1(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and A[i][j]:
                A[i][j] = 0
                dfs(i-1,j), dfs(i+1,j), dfs(i,j-1), dfs(i,j+1)
        for i in range(m): 
            dfs(i, 0), dfs(i, n-1)
        for j in range(n): 
            dfs(0, j), dfs(m-1, j)
        return sum(A[i][j] for i in range(m) for j in range(n))



import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().numEnclaves1
        self.assertEqual(func([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(func([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        self.assertEqual(func([
            [0,0,0,1,1,1,0,1,0,0],
            [1,1,0,0,0,1,0,1,1,1],
            [0,0,0,1,1,1,0,1,0,0],
            [0,1,1,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,0,0,1,0],
            [0,0,1,0,1,1,1,1,0,1],
            [0,1,1,0,0,0,1,1,1,1],
            [0,0,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,0],
            [0,0,0,0,1,1,0,0,0,1]]), 3)

if __name__ == "__main__":
    unittest.main()