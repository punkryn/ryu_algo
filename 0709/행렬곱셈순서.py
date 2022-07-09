# https://www.acmicpc.net/problem/11049
from sys import stdin

si = stdin.readline

if __name__ == '__main__':
    INF = int(1e10)
    n = int(si())
    matrix = [[0]] + [list(map(int, si().split())) for _ in range(n)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            x = j + i
            dp[j][x] = INF
            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])
    
    print(dp[1][n])