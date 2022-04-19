# https://www.acmicpc.net/problem/1912
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    
    dp = [[-1001] * 2 for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        # i번째를 선택하는데 연속하는 경우 vs 연속하지 않는 경우
        dp[i][0] = max(dp[i - 1][0] + a[i], a[i]) 
        # i번째를 선택 안 하는 경우
        dp[i][1] = max(dp[i - 1])
    print(max(dp[n-1]))