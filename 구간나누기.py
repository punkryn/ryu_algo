# https://www.acmicpc.net/problem/2228
import sys
si = sys.stdin.readline
INF = 33000
if __name__ == "__main__":
    n, m = map(int, si().split())
    a = [int(si()) for _ in range(n)]
    
    dp = [[-INF] * n for _ in range(m)]
    dp[0][0] = a[0]
    start, end = 0, 0
    for i in range(m):

        for j in range(i * 2, i * 2 + n - 2 ** (m - 1)):
            if i == 0 and j == 0: continue
            if i == 0:
                dp[i][j] = max(dp[i][j - 1] + a[j], a[j])
            else:
                dp[i][j] = max(dp[i - 1][j - 2] + a[j], dp[i][j - 1] + a[j])
                
    print(max(dp[-1]))