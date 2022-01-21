# https://acmicpc.net/problem/1149
import sys
si = sys.stdin.readline
INF = int(1e9)
def main():
    n = int(si())
    homes = [list(map(int, si().split())) for _ in range(n)]
    dp = [[INF, INF, INF] for _ in range(n + 1)]
    dp[1][0], dp[1][1], dp[1][2] = homes[0][0], homes[0][1], homes[0][2]

    for i in range(2, n + 1):
        for j in range(3):
            k1 = (j + 2) % 3
            k2 = (j + 1) % 3
            dp[i][j] = min(dp[i-1][k1] + homes[i-1][j], dp[i-1][k2] + homes[i-1][j])

    print(min(dp[n]))

if __name__ == '__main__':
    main()