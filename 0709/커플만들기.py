# https://www.acmicpc.net/problem/1727
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = sorted(map(int, si().split()))
    b = sorted(map(int, si().split()))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j:
                dp[i][j] = dp[i - 1][j - 1] + abs(a[i - 1] - b[j - 1])
            elif i > j:
                dp[i][j] = min(dp[i - 1][j - 1] + abs(a[i - 1] - b[j - 1]), dp[i - 1][j])
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + abs(a[i - 1] - b[j - 1]), dp[i][j - 1])
    print(dp[n][m])