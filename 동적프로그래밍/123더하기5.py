# https://www.acmicpc.net/problem/15990
import sys
si = sys.stdin.readline
MOD = 1000000009

if __name__ == '__main__':
    T = int(si())

    dp = [[0] * 4 for _ in range(100000 + 1)]
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1
    for i in range(4, 100001):
        for j in range(1, 4):
            if j == 1:
                dp[i][j] = (dp[i - j][2] + dp[i - j][3]) % MOD
            elif j == 2:
                dp[i][j] = (dp[i - j][1] + dp[i - j][3]) % MOD
            else:
                dp[i][j] = (dp[i - j][1] + dp[i - j][2]) % MOD

    for _ in range(T):
        n = int(si())
        print(sum(dp[n]) % MOD)