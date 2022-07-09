# https://www.acmicpc.net/problem/17069
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    h = [[1] * (n + 2)] + [[1] * (n + 2)] + [[1, 1] + list(map(int, si().split())) for _ in range(n)]
    dp = [[[0, 0, 0] for __ in range(n + 2)] for _ in range(n + 2)]
    dp[2][3][0] = 1

    for i in range(2, n + 2):
        for j in range(2, n + 2):
            if h[i][j] == 0:
                # -
                if h[i][j - 1] == 0 and h[i][j - 2] == 0:
                    dp[i][j][0] += dp[i][j - 1][0]
                    if h[i - 1][j - 1] == 0 and h[i - 1][j - 2] == 0:
                        dp[i][j][0] += dp[i][j - 1][1]

                # \
                if h[i][j - 1] == 0 and h[i - 1][j] == 0 and h[i - 1][j - 1] == 0:
                    if h[i - 1][j - 2] == 0:
                        dp[i][j][1] += dp[i - 1][j - 1][0]
                    if h[i - 1][j - 2] == 0 and h[i - 2][j - 2] == 0 and h[i - 2][j - 1] == 0:
                        dp[i][j][1] += dp[i - 1][j - 1][1]
                    if h[i - 2][j - 1] == 0:
                        dp[i][j][1] += dp[i - 1][j - 1][2]
                
                # |
                if h[i - 1][j] == 0 and h[i - 2][j] == 0:
                    dp[i][j][2] += dp[i - 1][j][2]
                    if h[i - 1][j - 1] == 0 and h[i - 2][j - 1] == 0:
                        dp[i][j][2] += dp[i - 1][j][1]
    
    print(sum(dp[n + 1][n + 1]))