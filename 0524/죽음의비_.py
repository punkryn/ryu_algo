# https://www.acmicpc.net/problem/22944
import sys
si = sys.stdin.readline

def dfs(x, y, hp, u, cur):
    global ans
    dist = abs(x - ex) + abs(y - ey)
    if dist <= hp + u:
        ans = min(ans, cur + dist)
        return
    
    for i in range(len(um)):
        if visited[i]: continue
        nx, ny = um[i]
        nd = abs(nx - x) + abs(ny - y)
        if nd > hp + u: continue
        k = nd - u
        k = max(0, k)
        visited[i] = True
        dfs(nx, ny, hp - k, d, cur + nd)
        visited[i] = False

if __name__ == '__main__':
    n, h, d = map(int, si().split())
    grid = [si().strip() for _ in range(n)]

    um = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'E':
                ex, ey = i, j
            elif grid[i][j] == 'U':
                um.append((i, j))
    
    visited = [False] * len(um)
    ans = int(1e9)
    dfs(sx, sy, h, 0, 0)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)