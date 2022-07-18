# https://www.acmicpc.net/problem/1926
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue
            if pic[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return cnt

if __name__ == '__main__':
    n, m = mis()
    pic = [list(mis()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if pic[i][j] == 0 or visited[i][j]:
                continue
            ans = max(ans, bfs(i, j))
            cnt += 1
    print(cnt)
    print(ans)