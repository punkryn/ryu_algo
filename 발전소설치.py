# https://www.acmicpc.net/problem/1277
import sys
from heapq import heappush, heappop
from math import floor, sqrt
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def dijkstra(x):
    q = [(0, x)]
    distance = [float('inf')] * (n + 1)
    distance[x] = 0
    prev = [(-1, 0) for _ in range(n + 1)]
    while q:
        cur_dist, cur = heappop(q)

        if distance[cur] < cur_dist:
            continue

        for dist, nxt in edges[cur]:
            nxt_dist = dist + cur_dist
            if nxt_dist < distance[nxt]:
                distance[nxt] = nxt_dist
                heappush(q, (nxt_dist, nxt))
                prev[nxt] = (cur, dist)
    
    return prev

if __name__ == '__main__':
    n, w = mis()
    m = float(si())
    coord = [list(mis()) for _ in range(n)]
    remain = set(tuple(mis()) for _ in range(w))
    edges = [[] for _ in range(n + 1)]
    flag = [False] * (n + 1)
    for x, y in remain:
        flag[x] = True
        flag[y] = True
        xi, yi = coord[x - 1][0], coord[x - 1][1]
        xj, yj = coord[y - 1][0], coord[y - 1][1]
        length = sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
        edges[x].append((length, y))
        edges[y].append((length, x))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if flag[i + 1] and flag[j + 1]: continue
            xi, yi = coord[i][0], coord[i][1]
            xj, yj = coord[j][0], coord[j][1]
            length = sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            if length > m: continue
            edges[i + 1].append((length, j + 1))
            edges[j + 1].append((length, i + 1))
    
    prev = dijkstra(1)
    idx = n
    total = 0
    while prev[idx][0] != -1:
        if not (flag[idx] and flag[prev[idx][0]]):
            total += prev[idx][1]
        idx = prev[idx][0]
    print(floor(total * 1000))