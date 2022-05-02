# https://www.acmicpc.net/problem/22944
# 7 2 2
# S.U....
# .......
# ..U....
# U.U....
# .......
# U......
# .U.U.UE
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, h, d = map(int, si().split())
    grid = [si().strip() for _ in range(n)]
    um = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'E':
                ex, ey = i, j
            elif grid[i][j] == 'U':
                um.append((i, j))
    
    q = deque()
    q.append((sx, sy, h, 0, 0))
    visited = [[[-1] * (len(um) + 1) for __ in range(n)] for _ in range(n)]
    visited[sx][sy][0] = 0
    while q:
        x, y, cur_hp, cur_um, cnt = q.popleft()
        
        if x == ex and y == ey:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if grid[nx][ny] == 'U':
                if cnt + 1 <= len(um) and visited[nx][ny][cnt + 1] == -1:
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cur_hp, d - 1, cnt + 1))
            elif grid[nx][ny] == '.':
                if cur_um > 0:
                    if visited[nx][ny][cnt] == -1:
                        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cur_hp, cur_um - 1, cnt))
                else:
                    if cur_hp > 1:
                        if visited[nx][ny][cnt] == -1:
                            visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                            q.append((nx, ny, cur_hp - 1, 0, cnt))
            elif grid[nx][ny] == 'E':
                if visited[nx][ny][cnt] == -1:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cur_hp, cur_um, cnt))
            abc=1
    
    ans = int(1e9)
    for i in visited[ex][ey]:
        if i == -1: continue
        ans = min(ans, i)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)