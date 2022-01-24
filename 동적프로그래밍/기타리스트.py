# https://www.acmicpc.net/problem/1495
import sys
si = sys.stdin.readline

def main():
    n, s, m = map(int, si().split())
    V = list(map(int, si().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][s] = 1

    for i in range(1, n + 1):
        ans = -1
        for j in range(m + 1):
            if dp[i-1][j] == 0:
                continue

            for k in [j - V[i-1], j + V[i-1]]:
                if k < 0 or k > m:
                    continue
                ans = max(ans, k)
                dp[i][k] += dp[i-1][j]

    print(ans)


if __name__ == '__main__':
    main()