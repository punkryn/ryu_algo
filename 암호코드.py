# https://www.acmicpc.net/problem/2011
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
MOD = 1000000
def go(x):
    if x in dp:
        return dp[x]
    
    if len(x) == 0:
        dp[x] = 0
        return 0

    if len(x) == 1:
        if x == '0':
            dp[x] = 0
            return 0
        dp[x] = 1
        return 1
    
    if len(x) == 2:
        x_ = int(x)
        if 10 < x_ < 20 or 20 < x_ <= 26:
            dp[x] = 2
            return 2
        elif 1 <= x_ <= 10 or x_ == 20:
            dp[x] = 1
            return 1
        else:
            if x[1] == '0':
                dp[x] = 0
                return 0
            else:
                dp[x] = 1
                return 1
    
    dp[x] = 0
    if x[0] != '0':
        if x[1] != '0':
            dp[x] = (dp[x] + go(x[1:])) % MOD
        if 10 <= int(x[:2]) <= 26:
            if x[2] != '0':
                dp[x] = (dp[x] + go(x[2:])) % MOD
    return dp[x]

if __name__ == '__main__':
    n = si().strip()
    dp = dict()
    print(go(n))