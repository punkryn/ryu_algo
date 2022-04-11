# https://www.acmicpc.net/problem/1753
import sys
import heapq
si = sys.stdin.readline
INF = int(1e6)
def dijkstra():
    distance = [INF] * (v + 1)
    distance[k] = 0
    q = []
    heapq.heappush(q, (0, k))

    while q:
        cur_cost, cur = heapq.heappop(q)

        if cur_cost > distance[cur]:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    return distance

if __name__ == '__main__':
    v, e = map(int, si().split())
    graph = [[] for _ in range(v + 1)]
    k = int(si())
    for _ in range(e):
        a, b, c = map(int, si().split())
        graph[a].append((b, c))

    for dist in dijkstra()[1:]:
        if dist == INF:
            print('INF')
        else:
            print(dist)