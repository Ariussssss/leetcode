# n个人，围在一起报数，报3的就出来，最后剩下谁？其实就是猴子报数问题

def monkey_count(n, out_idx = 3):
    arr = [x for x in range(n)]
    counter = 0
    l = len(arr)
    while l > 1:
        counter = (counter + out_idx - 1) % l
        arr.pop(counter)
        l -= 1
    return arr.pop()

import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = monkey_count
        # [0, 1, 2] 123
        # [0, 1] 45 6
        self.assertEqual(func(3), 1)
        # [0, 1, 2, 3] 123 4
        # [0, 1, 3] 56 7
        # [0, 3] 8 9
        self.assertEqual(func(4), 0)
        # [0, 1, 2, 3, 4, 5] 123 456
        # [0, 1, 3, 4] 789 10
        # [0, 1, 4] 1112 13
        # [0, 4] 1415
        self.assertEqual(func(6), 0)
        self.assertEqual(func(100), 90)
        self.assertEqual(func(4, 4), 1)

if __name__ == "__main__":
    unittest.main()

