# https://www.acmicpc.net/problem/2157
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

INF = int(1e9)

def go(x, cnt):
    if x == n:
        return 0
    if cnt == m:
        return -INF
    if dp[x][cnt] != -1:
        return dp[x][cnt]

    dp[x][cnt] = -INF
    for nxt, cost in info[x]:
        dp[x][cnt] = max(dp[x][cnt], go(nxt, cnt + 1) + cost)
    return dp[x][cnt]

if __name__ == '__main__':
    n, m, k = mis()
    info = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b, c = mis()
        if a > b: continue
        info[a].append((b, c))
    if n == 1:
        print(0)
        exit()
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    print(go(1, 1))
    # dp = [[0] * (n + 1) for _ in range(m + 1)]
    # for b, c in info[1]:
    #     dp[2][b] = max(dp[2][b], c)
    # for i in range(3, m + 1):
    #     for j in range(2, n + 1):
    #         if dp[i - 1][j] == 0: continue
    #         for b, c in info[j]:
    #             dp[i][b] = max(dp[i][b], dp[i - 1][j] + c)

    # print(max(dp[i][n] for i in range(m + 1)))