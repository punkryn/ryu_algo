# https://www.acmicpc.net/problem/2073
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

INF = int(1e9)

if __name__ == '__main__':
    d, p = mis()
    pipe = [list(mis()) for _ in range(p)]
    dp = [0] * (d + 1)
    dp[0] = INF
    for i in range(p):
        for j in range(d, -1, -1):
            k = j + pipe[i][0]
            if k > d: continue
            dp[k] = max(dp[k], min(dp[j], pipe[i][1]))
    print(dp[d])