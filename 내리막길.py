# https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m): continue
        if MAP[x][y] <= MAP[nx][ny]: continue
        dp[x][y] += dfs(nx, ny)
    return dp[x][y]

if __name__ == '__main__':
    n, m = mis()
    MAP = [list(mis()) for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]
    dp[n - 1][m - 1] = 1
    print(dfs(0, 0))