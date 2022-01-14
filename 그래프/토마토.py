# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def main():
    m, n, h = map(int, si().split())
    box = [[list(map(int, si().split())) for _ in range(n)] for _ in range(h)]
    q = deque()
    visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = 0
                elif box[i][j][k] == -1:
                    visited[i][j][k] = -2

    while q:
        cur = q.popleft()
        h_, n_, m_ = cur
        for i in range(6):
            nx = n_ + dx[i]
            ny = m_ + dy[i]
            nz = h_ + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if visited[nz][nx][ny] != -1: continue
                if box[nz][nx][ny] != 0: continue
                visited[nz][nx][ny] = visited[h_][n_][m_] + 1
                q.append((nz, nx, ny))
    ans = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == -1:
                    print(-1)
                    return
                ans = max(ans, visited[i][j][k])
    print(ans)

if __name__ == '__main__':
    main()