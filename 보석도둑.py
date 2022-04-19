# https://www.acmicpc.net/problem/1202
import sys
import heapq
si = sys.stdin.readline

if  __name__ == '__main__':
    n, k = map(int, si().split())
    jewels = sorted([list(map(int, si().split())) for _ in range(n)])
    bags = sorted([int(si()) for _ in range(k)])

    i = 0
    pq = []
    ans = 0
    for j in range(len(bags)):
        while i < len(jewels) and jewels[i][0] <= bags[j]:
            heapq.heappush(pq, -jewels[i][1])
            i += 1
        
        if pq:
            ans -= heapq.heappop(pq)
    print(ans)