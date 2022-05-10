# https://www.acmicpc.net/problem/1915
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [si().rstrip() for _ in range(n)]

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i - 1][j - 1] == '1':
                tmp = dp[i][j - 1] if grid[i - 1][j - 2] == '1' else 0
                tmp2 = tmp2 = dp[i - 1][j] if grid[i - 2][j - 1] == '1' else 0
                tmp3 = dp[i - 1][j - 1] if grid[i - 2][j - 2] == '1' else 0
                dp[i][j] = min(tmp, tmp2, tmp3) + 1
                ans = max(ans, dp[i][j])
    print(ans * ans)