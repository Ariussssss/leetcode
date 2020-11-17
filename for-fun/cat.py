# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-04-14 10:33:14


import sys
if __name__ == "__main__":
    # 读取第一行的n
    videos = []
    n = int(sys.stdin.readline().strip())
    for video in range(n):
        linecount = int(sys.stdin.readline().strip())
        a_video = []
        for i in range(linecount):
            line = sys.stdin.readline().strip()
            line = list(map(int, line.split()))
            a_video.append([
                (line[2 * x + 1], line[2 * x + 2])
                for x in range(line[0])
                ])
        videos.append(a_video)

    max_vectors = 0
    for video in videos:
        stack = {}
        for z in video:
            checked = []
            for vector in z:
                key = '{0}:{1}'.format(vector[0], vector[1])
                checked.append(key)
                if key in stack:
                    stack[key] += 1
                else:
                    stack[key] = 1
            delList = []
            for key in stack.keys():
                if key not in checked:
                    max_vectors = max(max_vectors, stack[key])
                    delList.append(key)
            for key in delList:
                del stack[key]
    print(max_vectors if max_vectors > 1 else 1)