# https://www.acmicpc.net/problem/17135
from sys import stdin
from itertools import combinations
si = stdin.readline

def attack(x, y, removed):
    cand = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist = abs(x - i) + abs(y - j)
                if dist <= d:
                    cand.append((dist, i, j))
    cand.sort(key=lambda x: (x[0], x[2]))
    if cand:
        removed.add((cand[0][1], cand[0][2]))

def move():
    cand = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
                if i + 1 < n:
                    cand.append((i + 1, j))
    
    for x, y in cand:
        grid[x][y] = 1
    return cand

if __name__ == '__main__':
    n, m, d = map(int, si().split())
    grid_ori = [list(map(int, si().split())) for _ in range(n)]

    cnt_ori = 0
    for i in range(n):
        for j in range(m):
            if grid_ori[i][j] == 1:
                cnt_ori += 1

    castle = [(n, y) for y in range(m)]
    answer = 0
    for comb in combinations(castle, 3):
        ans = 0
        cnt = cnt_ori
        grid = [row[:] for row in grid_ori]
        while cnt:
            removed = set()
            for x, y in comb:
                attack(x, y, removed)
            for x, y in removed:
                grid[x][y] = 0
            ans += len(removed)

            cnt = move()
        answer = max(answer, ans)
    print(answer)