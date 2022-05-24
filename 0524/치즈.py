# https://www.acmicpc.net/problem/2638
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != 0:
                continue
            
            if grid[nx][ny] != 0:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))
    
def find_outbound():
    visited = [[0] * m for _ in range(n)]
    for i in range(m):
        if visited[0][i]: continue
        BFS(0, i, visited)
    
    for j in [0, m - 1]:
        for i in range(1, n - 1):
            if visited[i][j]: continue
            BFS(i, j, visited)
    
    for i in range(m):
        if visited[n - 1][i]: continue
        BFS(n - 1, i, visited)
    return visited

def remove(out, cnt):
    cand = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 0:
                continue
                
            tmp = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if grid[ni][nj] == 0 and out[ni][nj] == 1:
                    tmp += 1
            
            if tmp >= 2:
                cand.append((i, j))
    
    for x, y in cand:
        grid[x][y] = 0
    
    return cnt - len(cand)

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [list(map(int, si().split())) for _ in range(n)]
    
    cnt = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 1:
                cnt += 1
    
    ans = 0
    while cnt:
        ans += 1
        out = find_outbound()
        cnt = remove(out, cnt)
    print(ans)