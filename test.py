def solution(y_idx, x_idx, p):
    target = (y_idx-1,x_idx-1)
    def dfs(y, x):
        if y == y_idx or x == x_idx or (y, x) == p:
            return 0
        elif (y, x) == target:
            return 1
        else:
            return dfs(y+1,x) + dfs(y,x+1)
    return dfs(0,0)
if __name__ == '__main__':
    print(solution(6, 8, (2, 4)))