import sys
import heapq
si = sys.stdin.readline
INF = int(1e9)

def main():
    n = int(si())
    m = int(si())
    bus = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, si().split())
        bus[a].append((c, b))
    
    start, end = map(int, si().split())

    q = []
    heapq.heappush(q, (0, start))
    distance = [[INF, 0] for _ in range(n + 1)]
    distance[start][0] = 0
    while q:
        cost, cur = heapq.heappop(q)
        if cost > distance[cur][0]:
            continue

        for nxt_cost, nxt in bus[cur]:
            if distance[nxt][0] > nxt_cost + distance[cur][0]:
                distance[nxt][0] = nxt_cost + distance[cur][0]
                heapq.heappush(q, (distance[nxt][0], nxt))
                distance[nxt][1] = cur

    print(distance[end][0])

    def go(s, cnt):
        if distance[s][1] == 0:
            print(cnt)
            print(s, end=' ')
            return
        
        go(distance[s][1], cnt + 1)
        print(s, end=' ')

    go(end, 1)

if __name__ == '__main__':
    main()
