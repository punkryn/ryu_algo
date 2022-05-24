# https://www.acmicpc.net/problem/11286
import sys
si = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n = int(si())
    a = []
    b = []
    for _ in range(n):
        x = int(si())
        if x == 0:
            if not a and not b:
                print(0)
            elif not a:
                print(heapq.heappop(b))
            elif not b:
                print(-heapq.heappop(a))
            else:
                if abs(a[0]) < abs(b[0]):
                    print(-heapq.heappop(a))
                elif abs(a[0]) > abs(b[0]):
                    print(heapq.heappop(b))
                else:
                    print(-heapq.heappop(a))
        else:
            if x > 0:
                heapq.heappush(b, x)
            else:
                heapq.heappush(a, -x)