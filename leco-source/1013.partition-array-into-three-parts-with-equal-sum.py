"""
1013.Partition Array Into Three Parts With Equal Sum

Difficulty: Easy
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 
Example 1:


Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1


Example 2:


Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false


Example 3:


Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


 
Constraints:


	3 <= arr.length <= 5 * 104
	-104 <= arr[i] <= 104



Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""

class Solution:
    @staticmethod
    def partSum(arr):
        sum_dict = {}
        def getData(x, y):
            key = '{0}:{1}'.format(x, y)
            if key not in sum_dict:
                sum_dict[key] = sum(arr[x:y])
            return sum(arr[x:y])
        length = len(arr)
        left = 0
        while left < length:
            right = length
            while right >= left:
                ll, ml, rl = getData(0, left), getData(left, right),\
                    getData(right, length)
                if ll == ml and ml == rl:
                    return True
                right -= 1
            left += 1
        return False

    @staticmethod
    def canPartSum(arr):
        s = sum(arr)
        if s % 3 == 0:
            s /= 3
            targets = [2 * s, s]
            res = 0
            for a in arr:
                res += a
                if res == targets[-1]:
                    targets.pop()
                if not targets:
                    return True
        return False

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().canPartSum
        self.assertEqual(func([1, 1, 1]), True)
        self.assertEqual(func([0,2,1,-6,6,7,9,-1,2,0,1]), False)
        self.assertEqual(func([0,2,1,-6,6,-7,9,1,2,0,1]), True)
        self.assertEqual(func([0,2,1,-6,6,7,9,-1,2,0,1]), False)


if __name__ == "__main__":
    unittest.main()
