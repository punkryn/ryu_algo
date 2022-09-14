# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    m, n = mis()
    box = [list(mis()) for _ in range(n)]

    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if box[i][j] != 1: continue
            q.append((i, j))
            visited[i][j] = 0
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny] != -1: continue

            if box[nx][ny] == -1: continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    
    ans = 0
    flag = False
    for i in range(n):
        for j in range(m):
            if box[i][j] == -1: continue
            if visited[i][j] == -1:
                flag = True
                break
            ans = max(ans, visited[i][j])
    
    print(ans if not flag else -1)