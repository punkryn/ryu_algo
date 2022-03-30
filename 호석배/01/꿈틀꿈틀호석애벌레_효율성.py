# https://www.acmicpc.net/problem/20167
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = list(map(int, si().split()))
    
    r = -1
    total = 0
    cand = []
    for i in range(n):
        flag = False
        while r + 1 < n and total < k:
            r += 1
            total += a[r]

        if total >= k:
            cand.append((i, r, total - k))
        total -= a[i]
    
    
    ans = 0
    pos = dict()
    for i in range(len(cand)):
        s, e, _ = cand[i]
        for j in range(s, e + 1):
            if j not in pos:
                pos[j] = i

    dp = [[0, 0] for _ in range(len(cand))]
    dp[0][0] = cand[0][2]
    dp[0][1] = 0
    for i in range(1, len(cand)):
        s, e, v = cand[i]
        if cand[i - 1][0] <= s <= cand[i - 1][1]:
            dp[i][0] = max(dp[i - 1])
        else:
            dp[i][0] = max(dp[i - 1]) + v
        
        if pos[s] > 0:
            dp[i][1] = max(dp[pos[s] - 1]) + v
        else:
            dp[i][1] = v
        ans = max(ans, dp[i][0], dp[i][1])
    
    print(ans)