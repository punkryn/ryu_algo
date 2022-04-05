# https://www.acmicpc.net/problem/1912
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    
    dp = [[-1001] * 2 for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0] + a[i], a[i])
        dp[i][1] = max(dp[i - 1])
    print(max(dp[n-1]))