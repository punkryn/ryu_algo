# https://www.acmicpc.net/problem/2228
import sys
si = sys.stdin.readline
INF = 33000
if __name__ == "__main__":
    n, m = map(int, si().split())
    a = [int(si()) for _ in range(n)]
    
    dp = [[-INF] * 2 for _ in range(n + 1) for _ in range(m + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j][0] = max(dp[i - 1][j])
            dp[i][j][1] = max(dp[i - 1][j - 1])