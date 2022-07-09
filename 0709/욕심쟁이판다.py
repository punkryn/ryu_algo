# https://www.acmicpc.net/problem/1937
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y):
    # flag = True
    # for i in range(4):
        # nx = x + dx[i]
        # ny = y + dy[i]
        # if not (0 <= nx < n and 0 <= ny < n): continue
        # if f[nx][ny] > f[x][y]:
        #     flag = False
        #     if visited[nx][ny]:
        #         visited[x][y] = max(visited[x][y], visited[nx][ny] + 1)
        #     else:
        #         go(nx, ny)
        #         visited[x][y] = max(visited[x][y], visited[nx][ny] + 1)
    
    # if flag:
    #     visited[x][y] = 1
    if visited[x][y] != 0:
        return visited[x][y]
    
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n): continue
        if f[nx][ny] > f[x][y]:
            visited[x][y] = max(visited[x][y], go(nx, ny) + 1)
    return visited[x][y]

if __name__ == '__main__':
    n = int(si())
    f = [list(map(int, si().split())) for _ in range(n)]
    
    visited = [[0] * n for _ in range(n)]
    ans = 0
    
    for i in range(n):
        for j in range(n):
            ans = max(ans, go(i, j))
    print(ans)