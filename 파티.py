# https://www.acmicpc.net/problem/1238
import sys
import heapq
si = sys.stdin.readline
INF = int(1e6)
def dijkstra(x, graph):
    distance = [INF] * (n + 1)
    distance[x] = 0
    q = [(0, x)]
    while q:
        cur_cost, cur = heapq.heappop(q)

        if distance[cur] < cur_cost:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    
    return distance

if __name__ == '__main__':
    n, m, x = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, si().split())
        graph[s].append((e, c))
        rev_graph[e].append((s, c))
    
    x_to_start = dijkstra(x, graph)
    start_to_x = dijkstra(x, rev_graph)
    ans = 0
    for i in range(1, n + 1):
        if i == x: continue
        ans = max(ans, x_to_start[i] + start_to_x[i])
    print(ans)