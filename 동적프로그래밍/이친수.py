# https://acmicpc.net/problem/2193
import sys

def main():
    n = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    print(sum(dp[n]))

if __name__ == '__main__':
    main()