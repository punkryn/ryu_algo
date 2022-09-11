# https://www.acmicpc.net/problem/1743
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m, k = mis()
    MAP = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        r, c = mis()
        MAP[r][c] = 1
    
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if visited[i][j] or MAP[i][j] == 0: continue
            q = deque([(i, j)])
            visited[i][j] = True
            cnt = 0
            while q:
                x, y = q.popleft()
                cnt += 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not (1 <= nx <= n and 1 <= ny <= m) or visited[nx][ny]:
                        continue
                    if MAP[nx][ny] == 0: continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
            
            ans = max(ans, cnt)
    print(ans)