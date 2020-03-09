# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-19 23:58:12


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        low = []
        high = []
        mid = arr.pop()
        for x in arr:
            if x > mid:
                high.append(x)
            else:
                low.append(x)
        return quick_sort(low) + [mid] + quick_sort(high)
if __name__ == '__main__':
    print (quick_sort([30,50,57,77,62,78,94,80,84]))