# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-27 20:06:11


def buildGraph():
    return {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['h'],
        'c': ['b', 'g', 'e'],
        'd': ['i'],
        'e': ['a'],
    }


def bfs(graph, master, cb=lambda x: False):
    checked = []
    onLine = graph[master].copy()
    while len(onLine) > 0:
        print (onLine)
        friend = onLine.pop(0)
        if friend in checked:
            continue
        else:
            checked.append(friend)
            if cb(friend):
                return checked
            if friend in graph.keys():
                onLine += graph[friend]

def dfs(graph, master, cb=lambda x: False):
    checked = []
    def _dfs(graph, now, cb):
        if now not in checked and now in master:
            checked.append(now)
            cb(now)
            [_dfs(graph, x, cb) for x in master[now]]
    _dfs(graph, master, cb)


def find(x):
    def find_x(y):
        return y == x
    return find_x

if __name__ == '__main__':
    graph = buildGraph()
    # print(bfs(graph, 'a', find('f')))
    # print(bfs(graph, 'a', find('i')))
    # print(bfs(graph, 'a', find('b')))
    # print(bfs(graph, 'a', find('e')))
    # print(bfs(graph, 'a', print))
    print(dfs(graph, 'a', print))
