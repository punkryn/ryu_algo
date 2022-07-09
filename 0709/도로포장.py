# https://www.acmicpc.net/problem/1162
import sys
from heapq import heappush, heappop
si = sys.stdin.readline

if __name__ == '__main__':
    n, m, k = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, si().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    q = [(0, 1, 0)]
    distance = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    distance[1][0] = 0
    while q:
        cur_cost, cur, cnt = heappop(q)

        if cur_cost > distance[cur][cnt]:
            continue

        for nxt, nxt_cost in graph[cur]:
            cost = cur_cost + nxt_cost
            if cost < distance[nxt][cnt]:
                distance[nxt][cnt] = cost
                heappush(q, (cost, nxt, cnt))
            
            if cnt + 1 <= k:
                if cur_cost < distance[nxt][cnt + 1]:
                    distance[nxt][cnt + 1] = cur_cost
                    heappush(q, (cur_cost, nxt, cnt + 1))
    
    print(min(distance[n]))