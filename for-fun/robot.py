# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-04-14 10:59:30


import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    route = list(map(int, line.split()))
    e = 0
    for x in range(n - 1, -1, -1):
        e = (e + route[x]) / 2
    print(int(e) + 1 if e > int(e) else int(e))