# https://www.acmicpc.net/problem/1826
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    infos = []
    for _ in range(n):
        a, b = map(int, si().split())
        heapq.heappush(infos, (a, b))
    l, p = map(int, si().split())
    cnt = 0
    q = []
    while p < l:
        while infos and infos[0][0] <= p:
            dist, fuel = heapq.heappop(infos)
            heapq.heappush(q, (-fuel, dist))
        
        if q:
            f, _ = heapq.heappop(q)
            p += -f
            cnt += 1
        else:
            cnt = -1
            break
        
    print(cnt)