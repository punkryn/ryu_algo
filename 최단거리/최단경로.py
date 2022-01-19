# https://acmicpc.net/problem/1753
import sys
import heapq
si = sys.stdin.readline

def main():
    v, e = map(int, si().split())
    k = int(si())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, si().split())
        graph[a].append((c, b))

    D = [int(1e9)] * (v + 1)
    D[k] = 0
    
    q = []
    heapq.heappush(q, (0, k))
    while q:
        cost, cur = heapq.heappop(q)

        if cost > D[cur]:
            continue
            
        for dst, nxt in graph[cur]:
            if D[nxt] > D[cur] + dst:
                D[nxt] = D[cur] + dst
                heapq.heappush(q, (D[nxt], nxt))
    
    for i in range(1, v + 1):
        if D[i] == int(1e9):
            print('INF')
        else:
            print(D[i])

if __name__ == '__main__':
    main()