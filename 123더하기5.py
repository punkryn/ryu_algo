# https://www.acmicpc.net/problem/15990
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    MOD = 1000000009
    dp = [[0, 0, 0] for _ in range(100005)]
    dp[1][0], dp[2][1], dp[3][2] = 1, 1, 1
    for i in range(3, 100001):
        for j in [1, 2, 3]:
            dp[i][j - 1] += (sum(dp[i - j][:j - 1]) + sum(dp[i - j][j:])) % MOD
        
    for _ in range(int(si())):
        print(sum(dp[int(si())]) % MOD)