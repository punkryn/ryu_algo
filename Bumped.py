# https://www.acmicpc.net/problem/15422
import sys
from heapq import heappush, heappop
si = sys.stdin.readline

INF = int(1e10)

def dijkstra(start):
    q = [(0, start)]
    distance = [INF] * n
    distance[start] = 0

    while q:
        cur_cost, cur = heappop(q)
        
        if cur_cost > distance[cur]:
            continue

        for nxt, nxt_cost in graph[cur]:
            cost = cur_cost + nxt_cost
            if distance[nxt] > cost:
                distance[nxt] = cost
                heappush(q, (cost, nxt))
    return distance

if __name__ == '__main__':
    n, m, f, s, t = map(int, si().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, si().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    flight = [list(map(int, si().split())) for _ in range(f)]

    d = dijkstra(s)
    rev = dijkstra(t)
    ans = d[t]
    for u, v in flight:
        ans = min(ans, d[u] + rev[v])
    print(ans)