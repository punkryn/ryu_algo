# https://www.acmicpc.net/problem/2589
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, cnt):
    v = [[-1] * m for _ in range(n)]
    q = deque([(x, y)])
    v[x][y] = 0

    lx, ly = 0, 0
    length = 0
    while q:
        x, y = q.popleft()

        lx, ly = x, y
        length = max(length, v[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != cnt:
                continue
            if v[nx][ny] != -1:
                continue

            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))
    return lx, ly, length

if __name__ == '__main__':
    n, m = mis()
    MAP = [si().strip() for _ in range(n)]
    
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or MAP[i][j] == 'W':
                continue
            
            cnt += 1
            q = deque([(i, j)])
            visited[i][j] = cnt
            
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                        continue
                    if MAP[nx][ny] == 'W':
                        continue
                    
                    visited[nx][ny] = cnt
                    q.append((nx, ny))
    
    ans = 0
    while cnt:
        for i in range(n):
            for j in range(m):
                if visited[i][j] == cnt:
                    lx, ly, _ = bfs(i, j, cnt)
                    _, _, length = bfs(lx, ly, cnt)
                    ans = max(ans, length)
                    break
        cnt -= 1
    print(ans)