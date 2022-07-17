# https://www.acmicpc.net/problem/1939
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def deter(d):
    q = deque([s])
    visited = [False] * (n + 1)
    while q:
        cur = q.popleft()
        if visited[cur]: continue
        visited[cur] = True

        for nxt, cost in graph[cur]:
            if cost < d: continue
            q.append(nxt)
    return visited[e]

if __name__ == '__main__':
    n, m = mis()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = mis()
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, e = mis()

    l, r = 1, int(1e9)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if deter(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)