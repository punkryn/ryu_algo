# https://acmicpc.net/problem/1003
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0] = 1
    if n > 0:
        dp[1][1] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[n][0], dp[n][1])

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()