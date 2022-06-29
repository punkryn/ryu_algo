# https://www.acmicpc.net/problem/10217
import sys
from heapq import heappush, heappop
si = sys.stdin.readline

def main():
    n, m, k = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, si().split())
        graph[u].append((v, c, d))
    
    inf = float('inf')
    d = [[inf] * (m + 1) for _ in range(n + 1)]
    d[1][0] = 0
    q = [(0, 1, 0)]
    while q:
        cur_cost, cur, cur_m = heappop(q)

        if cur_cost > d[cur][cur_m]:
            continue

        for nxt, nxt_m, nxt_cost in graph[cur]:
            cost = nxt_cost + cur_cost
            mm = cur_m + nxt_m
            if mm <= m and cost < d[nxt][mm]:
                for i in range(mm , m + 1):
                    if d[nxt][i] > cost:
                        d[nxt][i] = cost
                    else:
                        break
                heappush(q, (cost, nxt, mm))
    
    if d[n][m] == inf:
        print('Poor KCM')
    else:
        print(d[n][m])


if __name__ == '__main__':
    for _ in range(int(si())):
        main()