# https://www.acmicpc.net/problem/14925
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    m, n = map(int, si().split())
    MAP = [list(map(int, si().split())) for _ in range(m)]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    ans = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if MAP[i - 1][j - 1] != 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
    print(ans)