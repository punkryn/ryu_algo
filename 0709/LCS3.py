# https://www.acmicpc.net/problem/1958
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    a = si().strip()
    b = si().strip()
    c = si().strip()

    la, lb, lc = len(a), len(b), len(c)
    dp = [[[0] * (lc + 1) for _ in range(lb + 1)] for __ in range(la + 1)]
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            for k in range(1, lc + 1):
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1], dp[i - 1][j - 1][k], dp[i - 1][j][k - 1], dp[i][j - 1][k - 1], dp[i - 1][j - 1][k - 1] + (1 if a[i - 1] == b[j - 1] == c[k - 1] else 0))
    print(dp[la][lb][lc])