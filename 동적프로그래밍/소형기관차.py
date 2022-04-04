# https://www.acmicpc.net/problem/2616
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = [0] + list(map(int, si().split()))
    k = int(si())

    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i]
    
    dp = [[0] * (n + 1) for _ in range(3)]
    for i in range(3):
        for j in range((i + 1) * k, n + 1):
            if i == 0:
                dp[i][j] = max(dp[i][j - 1], ps[j] - ps[j - k])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + ps[j] - ps[j - k])
    print(dp)
    
    print(dp[-1][-1])