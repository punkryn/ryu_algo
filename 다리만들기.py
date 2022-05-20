# https://www.acmicpc.net/problem/2146
from sys import stdin
from collections import deque
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, cnt):
    q = deque([(x, y)])
    visited[x][y] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue

            if MAP[nx][ny] == 0:
                continue
            
            visited[nx][ny] = cnt
            q.append((nx, ny))

def bfs2(x, y, start):
    q = deque([(x, y)])
    v = [[0] * n for _ in range(n)]
    v[x][y] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or v[nx][ny]:
                continue

            if MAP[nx][ny] != 0 and visited[nx][ny] != start:
                return v[x][y]
            
            if MAP[nx][ny] == 0:
                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))
    return int(1e9)

if __name__ == "__main__":
    n = int(si())
    MAP = [list(map(int, si().split())) for _ in range(n)]
    
    visited = [[0] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j, cnt)
    
    # for v in visited:
    #     print(v)

    visited_ocean = set()
    ans = int(1e9)
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 0: continue
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (0 <= ni < n and 0 <= nj < n):
                    continue

                if MAP[ni][nj] == 1 or (ni, nj) in visited_ocean:
                    continue

                visited_ocean.add((ni, nj))
                ans = min(ans, bfs2(ni, nj, visited[i][j]))
    print(ans)