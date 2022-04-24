# https://www.acmicpc.net/problem/1915
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [si().rstrip() for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = int(grid[0][i])
    for i in range(n):
        dp[i][0] = int(grid[i][0])
    
    ans = 1 if grid[0][0] == '1' else 0
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
    print(ans * ans)