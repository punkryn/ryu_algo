# https://www.acmicpc.net/problem/16195
import sys
si = sys.stdin.readline

MOD = 1000000009

if __name__ == '__main__':
    dp = [[0] * (1001) for _ in range(1001)]
    dp[0][0] = 1
    for i in range(1, 1001):
        for j in range(1, 1001):
            for k in range(1, 4):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
            dp[i][j] %= MOD

    for _ in range(int(si())):
        n, m = map(int, si().split())
        print(sum([dp[i][n] for i in range(m + 1)]) % MOD)