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

    q = deque([(0, 0)])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != -1:
                continue

            if maze[nx][ny] == '0':
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))
            else:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    print(visited[n - 1][m - 1])