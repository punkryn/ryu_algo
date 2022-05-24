# https://www.acmicpc.net/problem/17404
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    INF = int(1e9)
    n = int(si())
    ans = INF
    dp = [[INF] * 3 for _ in range(3)]
    a, b, c = map(int, si().split())
    dp[0][0], dp[1][1], dp[2][2] = a, b, c
    for _ in range(n - 1):
        a, b, c = map(int, si().split())
        dp = [[min(dp[i][1], dp[i][2]) + a, min(dp[i][0], dp[i][2]) + b, min(dp[i][0], dp[i][1]) + c] for i in range(3)]
    print(min(dp[i][j] for i in range(3) for j in range(3) if i != j))