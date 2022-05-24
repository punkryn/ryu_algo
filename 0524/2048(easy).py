# https://www.acmicpc.net/problem/12100
from sys import stdin
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(d, cur):
    isCollision = set()
    if d == 0:
        for i in range(1, n):
            for j in range(n):
                idx = i
                while idx - 1 >= 0:
                    if cur[idx - 1][j] == 0:
                        cur[idx - 1][j], cur[idx][j] = cur[idx][j], cur[idx - 1][j]
                    else:
                        if cur[idx - 1][j] == cur[idx][j] and (idx - 1, j) not in isCollision:
                            cur[idx - 1][j] += cur[idx][j]
                            cur[idx][j] = 0
                            isCollision.add((idx - 1, j))
                        break

                    idx -= 1
    elif d == 1:
        for j in range(n - 2, -1, -1):
            for i in range(n):
                idx = j
                while idx + 1 < n:
                    if cur[i][idx + 1] == 0:
                        cur[i][idx + 1], cur[i][idx] = cur[i][idx], cur[i][idx + 1]
                    else:
                        if cur[i][idx + 1] == cur[i][idx] and (i, idx + 1) not in isCollision:
                            cur[i][idx + 1] *= 2
                            cur[i][idx] = 0
                            isCollision.add((i, idx + 1))
                        break
                    idx += 1
    elif d == 2:
        for i in range(n - 2, -1, -1):
            for j in range(n):
                idx = i
                while idx + 1 < n:
                    if cur[idx + 1][j] == 0:
                        cur[idx + 1][j], cur[idx][j] = cur[idx][j], cur[idx + 1][j]
                    else:
                        if cur[idx + 1][j] == cur[idx][j] and (idx + 1, j) not in isCollision:
                            cur[idx + 1][j] *= 2
                            cur[idx][j] = 0
                            isCollision.add((idx + 1, j))
                        break
                    idx += 1
    else:
        for j in range(1, n):
            for i in range(n):
                idx = j
                while idx - 1 >= 0:
                    if cur[i][idx - 1] == 0:
                        cur[i][idx - 1], cur[i][idx] = cur[i][idx], cur[i][idx - 1]
                    else:
                        if cur[i][idx - 1] == cur[i][idx] and (i, idx - 1) not in isCollision:
                            cur[i][idx - 1] *= 2
                            cur[i][idx] = 0
                            isCollision.add((i, idx - 1))
                        break
                    idx -= 1
    return cur

def go(depth, cur):
    global ans
    if depth == 5:
        for x in range(n):
            for y in range(n):
                ans = max(ans, cur[x][y])
        return
    
    for i in range(4):
        tmp = [row[:] for row in cur]
        cur = move(i, cur)
        go(depth + 1, cur)
        cur = tmp

if __name__ == '__main__':
    n = int(si())
    board = [list(map(int, si().split())) for _ in range(n)]
    ans = 0
    go(0, board)
    print(ans)