# https://www.acmicpc.net/problem/20166
import sys
si = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def DFS(x, y, depth, cur):
    if depth == deep:
        return
    
    if cur in ans:
        ans[cur] += 1

    for i in range(8):
        nx = (x + dx[i]) % n
        ny = (y + dy[i]) % m
        
        DFS(nx, ny, depth + 1, cur + grid[nx][ny])

if __name__ == '__main__':
    n, m, k = map(int, si().split())
    grid = [si().strip() for _ in range(n)]
    gods = [si().strip() for _ in range(k)]

    ans = dict()
    deep = 0
    for god in gods:
        ans[god] = 0
        deep = max(deep, len(god))
    
    for i in range(n):
        for j in range(m):
            DFS(i, j, 0, grid[i][j])
    
    for god in gods:
        print(ans[god])