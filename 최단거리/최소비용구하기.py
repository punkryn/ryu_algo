# https://acmicpc.net/problem/1916
import sys
import heapq
si = sys.stdin.readline

def main():
    n = int(si())
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, si().split())
        graph[s].append((c, e))
    start, end = map(int, si().split())

    D = [float('inf')] * (n + 1)
    D[start] = 0
    q = [(0, start)]
    while q:
        cost, v = heapq.heappop(q)

        if cost > D[v]:
            continue

        for dist, nxt in graph[v]:
            if D[nxt] > D[v] + dist:
                D[nxt] = D[v] + dist
                heapq.heappush(q, (D[nxt], nxt))
    print(D[end])

if __name__ == '__main__':
    main()