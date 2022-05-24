# https://www.acmicpc.net/problem/7579
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    active = list(map(int, si().split()))
    costs = list(map(int, si().split()))
    s = sum(costs)
    dp = [0] * (s + 1)
    ans = int(1e9)
    for i in range(1, n + 1):
        for j in range(s, costs[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - costs[i - 1]] + active[i - 1])

            if dp[j] >= m:
                ans = min(ans, j)
    print(ans)