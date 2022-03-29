# https://www.acmicpc.net/problem/11051
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    MOD = 10007

    dp = [[0] * (i + 1) for i in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0: dp[i][j] = dp[i-1][j]
            elif j == i: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
    print(dp[n][k] % MOD)