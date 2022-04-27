# https://www.acmicpc.net/problem/14442
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m, k = map(int, si().split())
    MAP = [si().strip() for _ in range(n)]
    
    q = deque()
    q.append((0, 0, 0))
    visited = [[[-1] * (k + 1) for _ in range(m)] for __ in range(n)]
    for i in range(k + 1):
        visited[0][0][i] = 1
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny][cnt] != -1: continue
            if MAP[nx][ny] == '0':
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                q.append((nx, ny, cnt))
            else:
                if cnt + 1 <= k:
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt + 1))
    
    ans = int(1e9)
    for i in range(k + 1):
        if visited[n-1][m-1][i] != -1:
            ans = min(ans, visited[n-1][m-1][i])
    
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)