# https://www.acmicpc.net/problem/14852
# berlekamp massey
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    MOD = 1000000007

    dp = [[0] * 2 for _ in range(n + 1)]
    dp[1][0] = 2
    if n > 1:
        dp[2][0] = 7
        dp[2][1] = 1
    for i in range(3, n + 1):
        dp[i][1] = (dp[i - 3][0] + dp[i - 1][1]) % MOD
        dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 2][0] * 3 + dp[i][1] * 2) % MOD
    print(dp[n][0] % MOD)