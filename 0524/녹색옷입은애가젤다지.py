# https://www.acmicpc.net/problem/4485
import sys
import heapq
si = sys.stdin.readline

INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = cave[0][0]
    q = []
    q.append((cave[0][0], 0, 0))
    while q:
        cur_cost, x, y = heapq.heappop(q)
        if cur_cost > distance[x][y]: continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            nxt_cost = cur_cost + cave[nx][ny]
            if nxt_cost < distance[nx][ny]:
                distance[nx][ny] = nxt_cost
                heapq.heappush(q, (nxt_cost, nx, ny))
    return distance[n - 1][n - 1]


if __name__ == '__main__':
    cnt = 0
    while True:
        cnt += 1
        n = int(si())
        if n == 0:
            break

        cave = [list(map(int, si().split())) for _ in range(n)]
        print(f'Problem {cnt}: {dijkstra()}')