# https://www.acmicpc.net/problem/18500
# 반례
# 7 9
# ...xxxx..
# ...x.....
# .xxx..xxx
# .x.x....x
# .x.xxxx.x
# .x......x
# .x......x
# 2
# 5 7

import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

LR = 1
RL = 3

def throw(height, d):
    if d == LR:
        for i in range(c):
            if cave[height][i] == 'x':
                cave[height][i] = '.'
                return True
        return False
    else:
        for i in range(c - 1, -1, -1):
            if cave[height][i] == 'x':
                cave[height][i] = '.'
                return True
        return False

def isFloat():
    visited = [[0] * c for _ in range(r)]
    for i in range(c):
        if cave[-1][i] == '.' or visited[-1][i] != 0:
            continue
        DFS(r - 1, i, visited)
    for i in range(r):
        for j in range(c):
            if visited[i][j] != 0:
                continue
            
            if cave[i][j] == '.':
                continue

            return DFS(i, j, visited)

def fall(cluster):
    if not cluster:
        return

    for x, y in cluster:
        cave[x][y] = '.'
    for d in range(1, r + 1):
        for x, y in cluster:
            if x + d >= r or cave[x + d][y] == 'x':
                break
        else:
            continue
        d -= 1
        break
    for x, y in cluster:
        cave[x + d][y] = 'x'
    
    # cluster.sort(reverse=True)
    # min_length = 200
    # floor = dict()
    # for x, y in cluster:
    #     if y not in floor:
    #         floor[y] = x
    #     else:
    #         floor[y] = max(x, floor[y])
    
    # for key in floor:
    #     length = 0
    #     x = floor[key]
    #     y = key
    #     nx = x + 1
    #     while nx < r and cave[nx][y] == '.':
    #         nx += 1
    #         length += 1
    #     min_length = min(min_length, length)
    

    # for x, y in cluster:
    #     cave[x][y] = '.'
    #     cave[x + min_length][y] = 'x'

def DFS(x, y, visited):
    stack = []
    cluster = []
    stack.append((x, y))
    cluster.append((x, y))
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < r and 0 <= ny < c):
                continue

            if visited[nx][ny] != 0:
                continue

            if cave[nx][ny] == '.':
                continue

            visited[nx][ny] = 1
            stack.append((nx, ny))
            cluster.append((nx, ny))
    
    return cluster

if __name__ == '__main__':
    r, c = map(int, si().split())
    cave = [list(si().strip()) for _ in range(r)]
    n = int(si())
    queries = list(map(int, si().split()))

    for i in range(n):
        # left
        if i % 2 == 0:
            # 1. throw
            if not throw(r - queries[i], LR):
                continue

        # right
        else:
            if not throw(r - queries[i], RL):
                continue

        # 2. float ?
        # 3. fall
        fall(isFloat())

    for cav in cave:
        print(''.join(cav))