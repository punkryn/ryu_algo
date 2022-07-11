# https://www.acmicpc.net/problem/1106
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    c, n = mis()
    info = [list(mis()) for _ in range(n)]
    dp = [float('inf')] * (c + 1)
    dp[0] = 0
    for i in range(c):
        for j in range(n):
            cost, val = info[j]
            nxt = i + val
            if nxt > c:
                nxt = c
            dp[nxt] = min(dp[nxt], dp[i] + cost)
    print(dp[c])