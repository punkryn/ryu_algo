# https://www.acmicpc.net/problem/16922
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())

    dp = [set() for _ in range(1001)]
    dp[0].add(0)
    
    for i in range(1, n * 50 + 1):
        for j in [1, 5, 10, 50]:
            if i - j < 0: break
            for k in dp[i - j]:
                if k + 1 > 20 or k + 1 in dp[i]: continue
                dp[i].add(k + 1)
    
    ans = 0
    for i in range(1, n * 50 + 1):
        if n in dp[i]:
            ans += 1
    print(ans)