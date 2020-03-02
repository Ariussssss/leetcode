# 1005. Maximize Sum Of Array After K Negations
# Given an array A of integers, we must modify the array in the following way: 
# we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
# (We may choose the same index i multiple times.)

# Return the largest possible sum of the array after modifying it in this way.

 

# Example 1:
# ```
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# ```
# Example 2:
# ```
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# ```
# Example 3:
# ```
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
# ```

# Note:

# 1. 1 <= A.length <= 10000
# 2. 1 <= K <= 10000
# 3. -100 <= A[i] <= 100

from typing import List
import heapq

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        small = []
        big = []
        for a in A:
            if a >= 0:
                big.append(a)
            else:
                small.append(a)
        len_small = len(small)
        if len_small > 0:
            if K < len_small:
                small.sort()
                i = 0
                while K > i:
                    small[i] = -small[i]
                    i += 1
                return sum(big + small)
            else:
                K -= len_small
                if K % 2 == 0:
                    return sum(big) - sum(small)
                else:
                    big.sort()
                    if big[0] > - small[len_small - 1]:
                        small[-1] = -small[len_small - 1]
                    else:
                        big[0] = - big[0]
                    return sum(big) - sum(small)
        else:
            if K % 2 == 0:
                return sum(big)
            else:
                big.sort()
                big[0] = - big[0]
                return sum(big)

    def s(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, -heapq.heappop(A))
        return sum(A)

import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().s
        self.assertEqual(func([3, -1, 0, 2], 3), 6)
        self.assertEqual(func([-8,3,-5,-3,-5,-2],6), 22)
        

if __name__ == "__main__":
    unittest.main()