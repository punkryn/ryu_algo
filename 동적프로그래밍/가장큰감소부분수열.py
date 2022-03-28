# https://www.acmicpc.net/problem/17216
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))

    dp = [0] * (n + 1)
    for i in range(n):
        dp[i] = a[i]
    ans = a[0]
    for i in range(n):
        for j in range(i):
            if a[i] < a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])
            ans = max(ans, dp[i])
    print(ans)

