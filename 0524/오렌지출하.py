# https://www.acmicpc.net/problem/11985
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m, k = map(int, si().split())
    a = [int(si()) for _ in range(n)]
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i * k
    
    for i in range(n):
        minv, maxv = a[i], a[i]
        
        for j in range(1, m + 1):
            if i + j > n:
                break

            minv = min(minv, a[i + j - 1])
            maxv = max(maxv, a[i + j - 1])
            dp[i + j] = min(dp[i + j], dp[i] + k + j * (maxv - minv))
            print(dp)
    
    print(dp[n])