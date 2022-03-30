# https://www.acmicpc.net/problem/20168

import sys
import heapq
si = sys.stdin.readline

INF = int(1e9)
def dijkstra(mid):
    distance = [INF] * (n + 1)
    distance[a] = 0
    q = []
    heapq.heappush(q, (0, a))

    while q:
        cur_cost, cur = heapq.heappop(q)
        
        if cur_cost > distance[cur]:
            continue

        for cost, nxt in graph[cur]:
            if cost > mid: continue
            nxt_cost = cur_cost + cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                if nxt == b and distance[nxt] <= c:
                    return True
                heapq.heappush(q, (nxt_cost, nxt))
    return distance[b] <= c

if __name__ == "__main__":
    n, m, a, b, c = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, cost = map(int, si().split())
        graph[x].append((cost, y))
        graph[y].append((cost, x))

    l, r = 0, int(1e9)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        deter = dijkstra(mid)
        if deter:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans)