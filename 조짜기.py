# https://www.acmicpc.net/problem/2229
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    s = [0] + list(mis())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[j - 1] + abs(s[i] - s[j]))
    print(dp[n])