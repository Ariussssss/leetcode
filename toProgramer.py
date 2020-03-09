# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-04-14 10:01:34


import sys
if __name__ == "__main__":
    def check(sits, y, x):
        if sits[y][x] == 2:
            ys = [n for n in [y + 1, y - 1] if n > -1 and n < len(sits)]
            xs = [n for n in [x + 1, x - 1] if n > -1 and n < len(sits[0])]
            return [(y_idx, x)
                for y_idx in ys
                if sits[y_idx][x] == 1
                ] + [(y, x_idx)
                for x_idx in xs
                if sits[y][x_idx] == 1
                ]
        return []
    sits = []
    line = sys.stdin.readline().strip()
    while line:
        sits.append(list(map(int, line.split())))
        line = sys.stdin.readline().strip()

    flag = True
    res = 0
    now_check = []
    for y in range(len(sits)):
        for x in range(len(sits[0])):
            now_check += check(sits, y, x)
                
    while now_check:
        on_check = now_check
        now_check = []
        res += 1
        for location in on_check:
            y, x = location
            sits[y][x] = 2
        for location in on_check:
            y, x = location
            now_check += check(sits, y, x)

    for y in range(len(sits)):
        for x in range(len(sits[0])):
            if sits[y][x] == 1:
                flag = False
                print(-1)
    if flag:
        print(res)
