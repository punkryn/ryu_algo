# https://www.acmicpc.net/problem/5719
import sys
from heapq import heappush, heappop
from collections import deque
si = sys.stdin.readline

inf = float('inf')
def dijkstra(s, n, graph, check):
    q = [(0, s)]
    distance = [inf] * n
    distance[s] = 0
    while q:
        cur_cost, cur = heappop(q)

        if distance[cur] < cur_cost:
            continue

        for nxt, cost in graph[cur]:
            if check[cur][nxt] == False: continue
            nxt_cost = cost + cur_cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
            
    return distance

def main():
    n, m = map(int, si().split())
    if n == 0 and m == 0:
        exit()
    s, d = map(int, si().split())
    graph = [[] for _ in range(n)]
    trace = [[] for _ in range(n)]
    check = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, si().split())
        graph[u].append((v, p))
        trace[v].append((u, p))
        check[u][v] = True
    
    sd = dijkstra(s, n, graph, check)
    q = deque([(d, 0)])
    while q:
        cur, cur_cost = q.popleft()

        for nxt, cost in trace[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost + sd[nxt] == sd[d]:
                if check[nxt][cur]:
                    check[nxt][cur] = False
                    q.append((nxt, nxt_cost))

    sd = dijkstra(s, n, graph, check)
    print(sd[d] if sd[d] != inf else -1)

if __name__ == '__main__':
    while True:
        main()