# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-16 14:27:35

# 我们使用字典来表示社交网络的传播关系，键表示信息接受者，值表示信息发出者。
# 例如：g = {'b': 'a', 'c': 'a', 'd': 'b'}表示信息由a传到b和c，再由b传到d。
# 写出一个函数，这个函数接受这样任何一个传播关系的字典，返回这个传播关系的最远路径的级数(整型)。
# 例如，在给定的g这个例子中，最远路径的级数为2（从a到b，再从b到d）

def solution(path_dict):
    res = {}
    for x in path_dict.keys():
        if path_dict[x] in path_dict.keys():
            res[x] = 1 + res[path_dict[x]]
            del res[path_dict[x]]
            path_dict[x] = path_dict[path_dict[x]]
            del path_dict[path_dict[x]]
        else:
            if x in res:
                res[x] += 1
            else:
                res[x] = 1
    return max(res.values())

if __name__ == '__main__':
    g = dict({'b': 'a', 'c': 'a', 'd': 'b', 'f': 'd', 'e': 'c'})
    print solution(g)