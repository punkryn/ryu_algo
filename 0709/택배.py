# https://www.acmicpc.net/problem/1719
import sys
si = sys.stdin.readline

INF = int(1e9)

if __name__ == '__main__':
    n, m = map(int, si().split())

    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    ans = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, si().split())
        dp[a][b] = c
        dp[b][a] = c
        ans[a][b] = b
        ans[b][a] = a
    
    for i in range(n + 1):
        dp[i][i] = 0
        ans[i][i] = 0
    
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if i == j: continue
                tmp = dp[i][k] + dp[k][j]
                if dp[i][j] > tmp:
                    dp[i][j] = tmp
                    ans[i][j] = ans[i][k]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print('-', end=' ')
            else:
                print(ans[i][j], end=' ')
        print()