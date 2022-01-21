# https://acmicpc.net/problem/15988
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    T = int(si())
    dp = [0] * (1000000 + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, 1000001):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    for _ in range(T):
        n = int(si())
        print(dp[n] % 1000000009)