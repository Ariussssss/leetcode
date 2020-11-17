# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-04-14 10:59:30


import sys
if __name__ == "__main__":
    routes = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        routes.append(list(map(int, line.split())))

    checked = []
    citys = [x for x in range(n)]
    # 0 为北京
    def _dfs(checked):
        froms = checked[-2]
        to = checked[-1]
        if len(checked) == n:
            return routes[froms][to] + routes[to][0]
        return routes[froms][to] + min(_dfs(checked + [city])
            for city in citys
            if city not in checked)
    if n > 1:
        res = min(_dfs([0] + [city])
                for city in citys
                if city not in [0])
        print(res)
    else:
        print(0)
