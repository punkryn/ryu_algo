# https://www.acmicpc.net/problem/15992
from sys import stdin
si = stdin.readline
MOD = 1000000009

if __name__ == '__main__':
    dp = [[0] * (1000 + 1) for _ in range(1000 + 1)]
    dp[1][1], dp[1][2], dp[1][3] = 1, 1, 1
    for i in range(1, 1000):
        for j in range(1, 1001):
            for k in range(1, 4):
                if j + k <= 1000:
                    dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD
    for _ in range(int(si())):
        n, m = map(int, si().split())
        print(dp[m][n] % MOD)