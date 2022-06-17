# https://www.acmicpc.net/problem/1504
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = int(1e9)
def dijkstra(s, e, ev1, ev2):
    distance = [INF] * (n + 1)
    distance[s] = 0
    q = [(0, s)]
    while q:
        cur_cost, cur = heappop(q)

        if cur_cost < distance[cur]:
            continue
        
        for nxt, cost in graph[cur]:
            # if nxt == ev1 or nxt == ev2: continue
            nxt_cost = cur_cost + cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
    return distance[e]

if __name__ == '__main__':
    n, e = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, si().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, si().split())

    mid = dijkstra(v1, v2, 1, n)
    case1 = dijkstra(1, v1, v2, n) + mid + dijkstra(v2, n, 1, v1)
    case2 = dijkstra(1, v2, v1, n) + mid + dijkstra(v1, n, 1, v2)
    if case1 >= INF and case2 >= INF:
        print(-1)
    else:
        print(min(case1, case2))