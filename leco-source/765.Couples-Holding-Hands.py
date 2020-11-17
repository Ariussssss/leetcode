"""
765. Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.

"""

import unittest
from typing import List

class Solution:
    def isLeft(num: int):
        return num % 2 == 0

    def find_couple(half_num: int, mate: int,  row: List[int]):
        couple_num = half_num + (+1 if Solution.isLeft(half_num) else -1)
        # print(couple_num, Solution.isLeft(half_num), row)
        idx = row.index(couple_num)
        # same
        row[idx] = mate
        return row

    def minSwapsCouples(self, row: List[int]) -> int:
        # print(row)
        if len(row) < 4:
            return 0
        left = 0
        while left < len(row) and int(row[left] / 2) == int(row[left+1] / 2):
            left += 2
        if left >= len(row):
            return 0
        # print(left, left+1, row[left], row[left+1])
        left_couple = Solution.find_couple(row[left], row[left+1], row[left+2:])
        right_couple = Solution.find_couple(row[left+1], row[left], row[left+2:])
        return min(self.minSwapsCouples(left_couple), self.minSwapsCouples(right_couple)) + 1
        
class CouplesHoldingHandsCase(unittest.TestCase):
    def test_couples_holding_hands(self):
        s = Solution()
        for i, o in [([0, 2, 1, 3], 1), ([3, 2, 0, 1], 0), ([5,4,2,6,3,1,0,7], 2)]:
            self.assertEqual(s.minSwapsCouples(i), o)


if __name__ == '__main__':
    s = Solution()
    s.minSwapsCouples([5,4,2,6,3,1,0,7])
    unittest.main()

