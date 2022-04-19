# https://www.acmicpc.net/problem/11265
import sys
import heapq
si = sys.stdin.readline
INF = int(1e9)
def dijkstra(a, b, c):
    nxt_list = list(range(1, n + 1))
    distance = [INF] * (n + 1)
    distance[a] = 0
    q = []
    q.append((0, a))
    while q:
        cur_cost, cur = heapq.heappop(q)

        if distance[cur] < cur_cost:
            continue

        for nxt in nxt_list:
            if nxt == cur: continue
            nxt_cost = matrix[cur - 1][nxt - 1] + cur_cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    return distance[b] <= c

if __name__ == '__main__':
    n, m = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]

    # dp = [[INF] * n for _ in range(n)]
    # for i in range(n):
    #     dp[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    # print(matrix)

    for _ in range(m):
        a, b, c = map(int, si().split())
        # if dijkstra(a, b, c):
        if matrix[a - 1][b - 1] <= c:
            print('Enjoy other party')
        else:
            print('Stay here')