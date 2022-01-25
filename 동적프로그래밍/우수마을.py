# https://www.acmicpc.net/problem/1949
import sys
sys.setrecursionlimit(1000000)
si = sys.stdin.readline

def main():
    n = int(si())
    residents = [0] + list(map(int, si().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)

    # dp = [[0, 0] for _ in range(n + 1)]

    def dfs(x, prev):
        v1, v2 = residents[x], 0
        for nxt in graph[x]:
            if nxt == prev:
                continue

            t1, t2 = dfs(nxt, x)
            v1 = max(v1, v1 + t2)
            v2 = max(v2, v2 + t1, v2 + t2)

            # dp[nxt][0] = max(dp[x][1] + residents[nxt], dp[nxt][0])
            # dp[nxt][1] = max(dp[x][0], dp[nxt][1])

            # dfs(nxt, x)
        return v1, v2

    # dp[1][0] = residents[1]
    print(max(dfs(1, -1)))
    # print(dp)

if __name__ == '__main__':
    main()