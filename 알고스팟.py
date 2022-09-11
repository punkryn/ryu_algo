# https://www.acmicpc.net/problem/1261
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    m, n = mis()
    maze = [si().strip() for _ in range(n)]
    
    limit = n + m
    q = deque([(0, 0, 0)])
    visited = [[[-1] * limit for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0
    
    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if maze[nx][ny] == '0':
                if visited[nx][ny][cnt] != -1: continue
                visited[nx][ny][cnt] = visited[x][y][cnt]
                q.append((nx, ny, cnt))
            else:
                if cnt + 1 >= limit:
                    continue
                if visited[nx][ny][cnt + 1] != -1: continue
                visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                q.append((nx, ny, cnt + 1))
    
    ans = float('inf')
    for i in range(limit):
        if visited[n - 1][m - 1][i] == -1:
            continue
        
        ans = min(ans, visited[n - 1][m - 1][i])
    print(ans)