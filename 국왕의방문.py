# https://www.acmicpc.net/problem/2982
import sys
import heapq
si = sys.stdin.readline

INF = int(1e9)

def diijkstra():
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, a, k))
    dist[a] = 0

    while q:
        cur_cost, cur_node, cur_time = heapq.heappop(q)

        if cur_cost > dist[cur_node]:
            continue

        for nxt, cost in roads[cur_node]:
            nxt_cost = cost + cur_cost
            nxt_time = cur_time + cost
            s, e = lock[cur_node][nxt]
            if s <= cur_time <= e:
                nxt_cost += e - cur_time + 1
                nxt_time += e - cur_time + 1
                
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt, nxt_time))
    return dist[b]

if __name__ == '__main__':
    n, m = map(int, si().split())
    a, b, k, g = map(int, si().split())
    vertex = list(map(int, si().split()))
    roads = [[] for _ in range(n + 1)]
    edges = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, l = map(int, si().split())
        roads[u].append((v, l))
        roads[v].append((u, l))
        edges[u][v] = l
        edges[v][u] = l
    
    lock = [[[0, 0] for _ in range(n + 1)] for __ in range(n + 1)]
    start = 0
    for i in range(g - 1):
        lock[vertex[i]][vertex[i + 1]] = [start, start + edges[vertex[i]][vertex[i + 1]] - 1]
        lock[vertex[i + 1]][vertex[i]] = [start, start + edges[vertex[i]][vertex[i + 1]] - 1]
        start += edges[vertex[i]][vertex[i + 1]]
        
    print(diijkstra())