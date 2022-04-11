# https://www.acmicpc.net/problem/2623
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        orders = list(map(int, si().split()))
        for i in range(2, orders[0] + 1):
            degree[orders[i]] += 1
            graph[orders[i - 1]].append(orders[i])
    
    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
    
    ans = []
    while q:
        cur = q.popleft()

        ans.append(cur)

        for nxt in graph[cur]:
            degree[nxt] -= 1

            if degree[nxt] == 0:
                q.append(nxt)
    if len(ans) == n:
        for a in ans:
            print(a)
    else:
        print(0)