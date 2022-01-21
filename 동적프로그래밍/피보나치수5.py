# https://acmicpc.net/problem/10870
import sys
si = sys.stdin.readline
n = int(si())

dp = [0] * 21
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])