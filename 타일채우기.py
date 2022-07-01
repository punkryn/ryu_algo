# https://www.acmicpc.net/problem/2133
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    if n % 2 == 1:
        print(0)
        exit()
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 2:
        dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * dp[2]
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2
    print(dp[n])