# https://www.acmicpc.net/problem/2616
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    k = int(si())

    ps = []
    r = 0
    total = 0
    cnt = 0
    for l in range(n):
        while r < n and cnt < k:
            total += a[r]
            r += 1
            cnt += 1
        
        if cnt == k:
            ps.append(total)

        total -= a[l]
        cnt -= 1
    
    dp = [[[0, []], [0, []]] for _ in range(len(ps))]
    dp[0][0][0] = ps[0]
    dp[0][0][1].append((0, k - 1))
    for i in range(1, len(ps)):
        if i - k >= 0:
            if dp[i - k][0][0] > dp[i - k][1][0]:
                dp[i][0][0] = dp[i - k][0][0] + ps[i]
                dp[i][0][1] += dp[i - k][0][1]
                dp[i][0][1].append((i, i + k - 1))
            else:
                dp[i][0][0] = dp[i - k][1][0] + ps[i]
                dp[i][0][1] += dp[i - k][1][1]
                dp[i][0][1].append((i, i + k - 1))
        else:
            dp[i][0][0] = ps[i]
            dp[i][0][1].append((i, i + k - 1))
        
        dp[i][1] = max(dp[i-1])
        if dp[i - 1][0][0] > dp[i - 1][1][0]:
            dp[i][1][0] = dp[i - 1][0][0]
            dp[i][1][1] += dp[i-1][0][1]
        else:
            dp[i][1][0] = dp[i - 1][1][0]
            dp[i][1][1] += dp[i - 1][1][1]

    print(dp)