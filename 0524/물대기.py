# https://www.acmicpc.net/problem/1368
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    d = [int(si()) for _ in range(n)]
    costs = [list(map(int, si().split())) for _ in range(n)]

    q = []
    for i in range(n):
        heapq.heappush(q, (d[i], i))
    visited = [0] * n
    
    ans = 0
    cnt = n
    while cnt:
        cost, cur = heapq.heappop(q)

        if visited[cur]: continue
        visited[cur] = 1
        ans += cost
        cnt -= 1

        for i in range(n):
            if i == cur or visited[i]: continue
            heapq.heappush(q, (costs[cur][i], i))
    print(ans)