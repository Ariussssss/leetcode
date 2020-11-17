'''
一个数字中的每位只能交换一次，求可能的最大值
'''

def number_swap(num):
    checked = []
    val_list = []
    idx_list = []
    num_str = str(num)
    num_list = [int(x) for x in num_str]
    start = 0
    while len(num_list) > len(checked):
        max_num = 0
        max_idx = None
        for idx, x in enumerate(num_list):
            if idx not in checked:
                if max_num < x:
                    max_num = x
                    max_idx = [idx]
                elif max_num == x:
                    max_idx.append(idx)
        count = len(max_idx)
        join_idx = []
        while count:
            if start in checked:
                start += 1
                continue
            if start not in max_idx:
                join_idx.append(start)
                checked.append(start)
            start += 1
            count -= 1
        nl = [num_list[x] for x in join_idx]
        nl.sort(reverse=True)
        checked += max_idx
        val_list += [max_num for _ in max_idx] + nl
        idx_list += join_idx + max_idx
    res = ['' for x in range(0, len( num_list))]
    for idx, x in enumerate(idx_list):
        res[x] = val_list[idx]
    s = 0
    while res:
        i = res.pop(0)
        s = s * 10 + i
    return s

 
if __name__ == '__main__':
    print(5435312435)
    print(number_swap(5435312435))
    print(56891)
    print(number_swap(56891))
    print(10^2)