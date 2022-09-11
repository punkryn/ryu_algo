# https://www.acmicpc.net/problem/1726
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    n, m = mis()
    s = [list(mis()) for _ in range(n)]
    
    sr, sc ,sd = mis()
    er, ec, ed = mis()
    er, ec, ed = er - 1, ec - 1, ed - 1

    q = deque([(sr - 1, sc - 1, sd - 1)])
    visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]
    visited[sr - 1][sc - 1][sd - 1] = 0

    while q:
        x, y, d = q.popleft()

        if x == er and y == ec and d == ed:
            break

        for i in range(1, 4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny][d] != -1:
                continue

            if s[nx][ny] != 0: continue
            if i >= 2:
                if d == 0:
                    if sum(s[nx][y: ny + 1]) != 0: continue
                elif d == 1:
                    if sum(s[nx][ny: y + 1]) != 0: continue
                elif d == 2:
                    if sum([s[j][ny] for j in range(x, nx + 1)]) != 0: continue
                else:
                    if sum([s[j][ny] for j in range(nx, x + 1)]) != 0: continue

            visited[nx][ny][d] = visited[x][y][d] + 1
            q.append((nx, ny, d))

        for i in range(2):
            if d == 0:
                nd = [3, 2]
            elif d == 1:
                nd = [2, 3]
            elif d == 2:
                nd = [0, 1]
            else:
                nd = [1, 0]
            
            for nnd in nd:
                if visited[x][y][nnd] != -1: continue
                visited[x][y][nnd] = visited[x][y][d] + 1
                q.append((x, y, nnd))
    
    print(visited[er][ec][ed])