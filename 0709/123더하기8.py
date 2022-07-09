# https://www.acmicpc.net/problem/15993
from sys import stdin
si = stdin.readline
MOD = 1000000009
if __name__ == '__main__':
    dp = [[0] * 2 for _ in range(100001)]
    dp[0][1] = 1
    for i in range(1, 100001):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i][0] = (dp[i][0] + dp[i - j][1]) % MOD
                dp[i][1] = (dp[i][1] + dp[i - j][0]) % MOD
    for _ in range(int(si())):
        n = int(si())
        print(dp[n][0], dp[n][1])