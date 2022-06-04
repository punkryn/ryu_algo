# https://www.acmicpc.net/problem/1823
import sys
si = sys.stdin.readline

if __name__ == "__main__":
    n = int(si())
    v = [int(si()) for _ in range(n)]
    ans = 0
    dp = [[[0, 0] for _ in range(n)] for __ in range(n + 1)]
    dp[1][0][0], dp[1][-1][1] = v[0], v[-1]
    for i in range(2, n + 1):
        for j in range(n):
            cur = i * v[j]
            if j == 0:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][n - (i - 1)][1] + cur)
            else:
                if dp[i - 1][j - 1][0] != 0:
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][(n - (i - j - 1)) % n][1] + cur, dp[i - 1][j - 1][0] + cur)
            
            if j == n - 1:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][i - 2][1] + cur)
            else:
                if dp[i - 1][j + 1][1] != 0:
                    dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j + 1][1] + cur, dp[i - 1][i - (n - j + 1)][0] + cur)

    for d in dp:
        print(d)
    print(ans)