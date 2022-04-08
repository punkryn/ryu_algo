# https://www.acmicpc.net/problem/2637
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        x, y, k = map(int, si().split())
        graph[y].append((x, k))
        degree[x] += 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    q = deque()
    cand = set()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            cand.add(i)
    
    while q:
        print(q)
        cur = q.popleft()

        for nxt, cost in graph[cur]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

            if cur in cand:
                dp[nxt][cur] += cost
            else:
                for c in cand:
                    dp[nxt][cur] += (dp[cur][c] * cost)
    print(dp)