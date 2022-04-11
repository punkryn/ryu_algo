# https://www.acmicpc.net/problem/14442
import sys
from collections import deque
si = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    n, m ,k = map(int, si().split())
    MAP = [si().strip() for _ in range(n)]

    q = deque()
    q.append((0, 0, 0, 1))
    visited = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    ans = -1
    while q:
        x, y, cnt, prev = q.popleft()
        if x == n - 1 and y == m - 1:
            ans = prev
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny][cnt] == -1:
                if MAP[nx][ny] == '1':
                    if cnt < k:
                        visited[nx][ny][cnt + 1] = 1
                        q.append((nx, ny, cnt + 1, prev + 1))
                else:
                    visited[nx][ny][cnt] = 1
                    q.append((nx, ny, cnt, prev + 1))

    print(ans)