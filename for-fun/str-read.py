# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-30 17:26:08

"""
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。

现在给一串数字，给出有多少种可能的译码结果。




输入描述:
编码后数字串

输出描述:
可能的译码结果数

输入例子1:
12

输出例子1:
2

例子说明1:
2种可能的译码结果（”ab” 或”l”）

输入例子2:
31717126241541717

输出例子2:
192

例子说明2:
192种可能的译码结果
"""
import sys

def read_str_possable(str_to_read: str):
    res = {'0':0}
    x = 0
    while str_to_read not in res:
        if str_to_read in res:
            return
        if x < 1:
            res[str_to_read[:x+1]] = 1
        else:
            real = int(str_to_read[x - 1:x + 1])
            if real == 0:
                return 0
            elif real > 10 and real <= 26 and real != 20:
                if x > 1:
                    res[str_to_read[:x+1]] = res[str_to_read[:x]]\
                        + res[str_to_read[:x - 1]]
                else:
                    res[str_to_read[:x+1]] = 2
            else:
                res[str_to_read[:x+1]] = res[str_to_read[:x]]
        x += 1
    return res[str_to_read]

if __name__ == "__main__":
    # values = sys.stdin.readline().strip()
    # print (read_str_possable(values))
    print (read_str_possable('31717126241541717'))
    print (read_str_possable('72416145196211821232022471311148103136128331523141061051992231223'))
    print (read_str_possable('12'))
    print (read_str_possable('11'))
    print (read_str_possable('100'))
