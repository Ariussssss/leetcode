"""
评分分数不同
每个分数有他的礼物
打得比小的多
最少有多少个礼物
"""

def smallHeap(arr, root=None):
    left = 2 * root + 1
    right = left + 1
    length = len(arr)
    small = root
    if left < length and arr[small] > arr[left]:
        small = left
    if right < length and arr[small] > arr[right]:
        small = right
    if small != root:
        arr[root], arr[small] = arr[small], arr[root]

def buildSmallHeap(arr):
    end = int(len(arr) / 2)
    for x in range(end, -1, -1):
        smallHeap(arr, x)

def gift_count(score_list):
    last = None
    gift_sum = 0
    gift_level = 1
    # res = {}
    for x in range(0, len(score_list)):
        buildSmallHeap(score_list)
        tmp = last
        last = score_list.pop(0)
        if tmp and tmp != last:
            gift_level += 1
        gift_sum += gift_level
        # if last in res:
        #     res[last] += gift_level
        # else:
        #     res[last] = gift_level
    # print(res)
    return gift_sum

import unittest

class TestSolution(unittest.TestCase):
    def test_filter_str(self):
        fn = gift_count
        self.assertEqual(fn([9]), 1)
        self.assertEqual(fn([9, 9]), 2)
        self.assertEqual(fn([9, 9, 8]), 5)
        self.assertEqual(fn([9, 7, 8]), 6)
        self.assertEqual(fn([9, 9, 7, 8]), 9)
        self.assertEqual(fn([9, 9, 7, 8,1,23,54,76,564,1,23,543]), 55)

if __name__ == '__main__':
    unittest.main()
