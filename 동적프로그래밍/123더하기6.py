# https://acmicpc.net/problem/15991
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    T = int(si())
    dp = [0] * 100005
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
    for i in range(4, 100002):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

    for _ in range(T):
        x = int(si())
        
        res = 0
        for mid in range(4):
            if x - mid >= 0 and (x - mid) % 2 == 0:
                res += dp[(x-mid)//2]
        
        print(res % 1000000009)
