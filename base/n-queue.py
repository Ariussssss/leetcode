# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-30 20:06:19


def n_queue(n: int):
    for x in range(0, n):
        for y in range(0, n):
            pass

def check(tree_arr, idx):
    if True:
        tree_arr[idx] = 1
    else:
        tree_arr[idx] = -1

def next(tree_arr, idx):
    status = tree_arr[idx]
    if status == 1:
        count = 1
        if idx * 4 + count > len(tree_arr):
            return True
        else:
            while count < 5:
                nextIdx = idx * 4 + count
                if tree_arr[nextIdx] == 0:
                    return nextIdx
                count += 1
    return int((idx - 1) / 4)

class Tree:
    def __init__(self, root=None, children=[]):
        self.root = root
        self.children = children
        self.status = 0

def buildTree():
    pass


def printTree(tree_arr: list):
    line = [0]
    while len(line) > 0:
        print(' '.join([str(tree_arr[x]) for x in line]))
        new_line = []
        for i in line: 
            for new_line_idx in [i * 4 + idx for idx in range(1, 5)]:
                if new_line_idx < len(tree_arr):
                    new_line.append(new_line_idx)
            line = new_line

if __name__ == '__main__':
    res = [0 for x in range(0, 4 * 4)]
    printTree(res)
    
