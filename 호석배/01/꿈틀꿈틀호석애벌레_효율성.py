# https://www.acmicpc.net/problem/20167
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = [0] + list(map(int, si().split()))
    
    r = 1
    total = 0
    lmax, ans = 0, 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        lmax = max(lmax, dp[i - 1])
        while r <= n and total < k:
            total += a[r]
            r += 1
        if total >= k:
            dp[r - 1] = max(dp[r - 1], lmax + total - k)
        else:
            break

        total -= a[i]

    for i in range(1, n + 1):
        ans = max(ans, dp[i])
    print(ans)