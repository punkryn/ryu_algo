# https://www.acmicpc.net/problem/2624
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    t = int(si())
    k = int(si())
    coins = [list(mis()) for _ in range(k)]
    
    dp = [0] * (t + 1)
    dp[0] = 1

    for i in range(k):
        p, n = coins[i]
        
        for j in range(t, -1, -1):
            for k in range(1, n + 1):
                if j - p * k >= 0:
                    dp[j] += dp[j - p * k]
    print(dp[t])