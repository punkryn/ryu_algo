# https://www.acmicpc.net/problem/11909
import sys
si = sys.stdin.readline

def main():
    INF = int(1e9)
    n = int(si())
    a = [list(map(int, si().split())) for _ in range(n)]
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i - 1 < 0:
                dp[i][j] = dp[i][j - 1] + (a[i][j] - a[i][j - 1] + 1 if a[i][j] >= a[i][j - 1] else 0)
            elif j - 1 < 0:
                dp[i][j] = dp[i - 1][j] + (a[i][j] - a[i - 1][j] + 1 if a[i][j] >= a[i - 1][j] else 0)
            else:
                dp[i][j] = min(dp[i][j - 1] + (a[i][j] - a[i][j - 1] + 1 if a[i][j] >= a[i][j - 1] else 0), dp[i - 1][j] + (a[i][j] - a[i - 1][j] + 1 if a[i][j] >= a[i - 1][j] else 0))
    print(dp[n-1][n-1])

if __name__ == "__main__":
    main()