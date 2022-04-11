# https://www.acmicpc.net/problem/15989
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    dp = [0] * 10005
    dp[0] = 1
    for i in range(1, 4):
        for j in range(i, 10001):
            dp[j] += dp[j - i]
    
    for _ in range(int(si())):
        print(dp[int(si())])