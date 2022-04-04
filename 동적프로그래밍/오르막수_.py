# https://www.acmicpc.net/problem/11057
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    MOD = 10007
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1
    
    for i in range(2, n + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][j:]) % MOD
    print(sum(dp[n]) % MOD)