# https://www.acmicpc.net/problem/2579
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    scores = [int(si()) for _ in range(n)]
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0], dp[0][1] = scores[0], 0
    if n >= 2:
        dp[1][0], dp[1][1] = scores[0] + scores[1], scores[1]

    for i in range(2, n):
        dp[i][0] = dp[i-1][1] + scores[i]
        dp[i][1] = max(dp[i-2][0] + scores[i], dp[i-2][1] + scores[i])
    print(max(dp[n-1][0], dp[n-1][1]))

if __name__ == '__main__':
    main()