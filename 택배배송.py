# https://www.acmicpc.net/problem/5972

import sys
import heapq
si = sys.stdin.readline
INF = int(1e9)
def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance = [INF] * (n + 1)
    distance[1] = 0

    while q:
        cur_cost, cur = heapq.heappop(q)
        
        if cur_cost > distance[cur]:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    return distance[n]

if __name__ == '__main__':
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, si().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    print(dijkstra())