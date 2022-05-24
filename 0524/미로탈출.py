# https://www.acmicpc.net/problem/14923
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

if __name__ == '__main__':
    n, m = map(int, si().split())
    hx, hy = map(int, si().split())
    ex, ey = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    
    visited = [[[-1] * 2 for _ in range(m)] for __ in range(n)]
    q = deque()
    q.append((hx-1, hy-1, 0))
    visited[hx-1][hy-1][0] = 0
    visited[hx-1][hy-1][1] = 0
    while q:
        x, y, cnt = q.popleft()

        if x == ex - 1 and y == ey - 1:
            if visited[x][y][0] != -1:
                print(visited[x][y][0])
            else:
                print(visited[x][y][1])
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m): 
                continue
            if visited[nx][ny][cnt] != -1: 
                continue

            if matrix[nx][ny] == 0:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                q.append((nx, ny, cnt))
            else:
                if cnt + 1 < 2:
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt + 1))
        
    print(-1)