# https://www.acmicpc.net/problem/1956
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = int(1e9)

if __name__ == '__main__':
    v, e = mis()
    dp = [[INF] * (v + 1) for _ in range(v + 1)]
    rev = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = mis()
        dp[a][b] = c
        rev[b].append((a, c))
    for i in range(v + 1):
        dp[i][i] = 0
    
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if i == j: continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans = INF
    for i in range(1, v + 1):
        for j, c in rev[i]:
            ans = min(ans, dp[i][j] + c)
    
    print(ans if ans < INF else -1)