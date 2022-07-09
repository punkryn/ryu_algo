# https://www.acmicpc.net/problem/2014
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    k, n = mis()
    p = list(mis())
    hq = []
    for p_ in p:
        heappush(hq, p_)
    
    top = 0
    prev = 0
    for i in range(n):
        top = heappop(hq)
        for j in range(k):
            val = p[j] * top
            heappush(hq, val)

            if top % p[j] == 0:
                break
    print(top)