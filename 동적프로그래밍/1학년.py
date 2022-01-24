# https://www.acmicpc.net/problem/5557
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    seq = list(map(int, si().split()))

    dp = [[0] * 21 for _ in range(n + 1)]
    dp[1][seq[0]] = 1

    for i in range(2, n):
        for j in range(21):
            if dp[i-1][j] == 0:
                continue

            if j - seq[i-1] >= 0:
                dp[i][j - seq[i-1]] += dp[i-1][j]
            if j + seq[i-1] <= 20:
                dp[i][j + seq[i-1]] += dp[i-1][j]

    print(dp[n-1][seq[-1]])

if __name__ == '__main__':
    main()