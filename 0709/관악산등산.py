# https://www.acmicpc.net/problem/14699
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline

def DFS(x):
    if dp[x] != 0:
        return dp[x]
    
    dp[x] = 1
    for nxt in graph[x]:
        if h[x] > h[nxt]: continue
        dp[x] = max(dp[x], DFS(nxt) + 1)
    return dp[x]

if __name__ == '__main__':
    n, m = map(int, si().split())
    h = [0] + list(map(int, si().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)

    dp = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        DFS(i)
        print(dp[i])