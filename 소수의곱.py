# https://www.acmicpc.net/problem/2014
import sys
from heapq import heappush, heappop, heapify
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    k, n = mis()
    p = list(mis())
    q = []
    for p_ in p:
        heappush(q, p_)
    top = 0
    for i in range(n):
        top = heappop(q)
        for j in range(k):
            val = top * p[j]
            heappush(q, val)

            if top % p[j] == 0:
                break
    print(top)