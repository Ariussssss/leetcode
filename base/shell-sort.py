# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-20 00:08:32


def shellSort(arr):
    l = len(arr)
    gap = 3
    while gap > 0:
        for x in range(0,gap):
            j = x + gap
            while j < l:
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j += gap
        gap -= 1
    return arr


if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print (shellSort(a))