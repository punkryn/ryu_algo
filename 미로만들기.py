# https://www.acmicpc.net/problem/2665
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    m = [si().strip() for _ in range(n)]
    
    visited = [[-1] * n for _ in range(n)]
    
    q = deque([(0, 0)])
    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == n - 1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny] != -1: continue

            if m[nx][ny] == '1':
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    print(visited[n - 1][n - 1])