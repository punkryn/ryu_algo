# https://www.acmicpc.net/problem/2293
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    coin = [int(si()) for _ in range(n)]
    dp = [0] * (k + 1)
    dp[0] = 1
    for c in coin:
        for i in range(1, k + 1):
            if i - c >= 0:
                dp[i] += dp[i - c]
    print(dp[-1])