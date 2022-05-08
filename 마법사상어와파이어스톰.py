# https://www.acmicpc.net/problem/20058
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate(i, j, L):
    s = 2 ** L
    tmp = [[0] * s for _ in range(s)]
    for x in range(i, i + s):
        for y in range(j, j + s):
            tmp[x - i][y - j] = grid[x][y]
    
    for x in range(s):
        for y in range(s):
            grid[y + i][len(tmp) - x - 1 + j] = tmp[x][y]

def reduce():
    cand = []
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0: continue
            cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (0 <= ni < length and 0 <= nj < length):
                    continue

                if grid[ni][nj] > 0:
                    cnt += 1
            
            if cnt < 3:
                cand.append((i, j))                
    
    for i, j in cand:
        grid[i][j] -= 1

def grid_sum():
    total = 0
    for i in range(length):
        for j in range(length):
            total += grid[i][j]
    return total

def BFS(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < length and 0 <= ny < length) or visited[nx][ny] or grid[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))
    return cnt

if __name__ == '__main__':
    n, q = map(int, si().split())
    length = 2 ** n
    grid = [list(map(int, si().split())) for _ in range(length)]
    stage = list(map(int, si().split()))
    for L in stage:
        for i in range(0, length, 2 ** L):
            for j in range(0, length, 2 ** L):
                rotate(i, j, L)
        reduce()
    
    print(grid_sum())

    visited = [[False] * length for _ in range(length)]
    ans = 0
    for i in range(length):
        for j in range(length):
            if visited[i][j] or grid[i][j] == 0: continue
            ans = max(ans, BFS(i, j))
    print(ans)