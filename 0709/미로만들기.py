# https://www.acmicpc.net/problem/2665
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    MAP = [si().strip() for _ in range(n)]
    black = sum([1 for i in range(n) for j in range(n) if MAP[i][j] == '0'])
    visited = [[[False] * (black + 1) for _ in range(n)] for __ in range(n)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = True
    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            if MAP[nx][ny] == '1' and visited[nx][ny][cnt] == False:
                visited[nx][ny][cnt] = True
                q.append((nx, ny, cnt))
            elif MAP[nx][ny] == '0' and cnt + 1 <= black and visited[nx][ny][cnt + 1] == False:
                visited[nx][ny][cnt + 1] = True
                q.append((nx, ny, cnt + 1))
    
    for i in range(black):
        if visited[n - 1][n - 1][i]:
            print(i)
            break