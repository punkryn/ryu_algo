# https://yabmoons.tistory.com/337
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    t = [0] * (n + 2)
    p = [0] * (n + 2)
    for i in range(1, n + 1):
        a, b = map(int, si().split())
        t[i] = a
        p[i] = b
    
    dp = [0] * (n + 2)
    ans = 0
    for i in range(1, n + 2):
        nxt = i + t[i]
        ans = max(ans, dp[i])
        if nxt <= n + 1:
            dp[nxt] = max(dp[nxt], ans + p[i])
    print(ans)