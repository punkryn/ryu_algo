# https://www.acmicpc.net/problem/2357
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def init():
    for i in range(height - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            seg[j] = [min(seg[j << 1][0], seg[j << 1 | 1][0]), max(seg[j << 1][1], seg[j << 1 | 1][1])]

def query(a, b):
    ret_min = float('inf')
    ret_max = 0
    a += (1 << height) - 1
    b += (1 << height) - 1
    while a <= b:
        if a & 1:
            ret_min = min(ret_min, seg[a][0]) 
            ret_max = max(ret_max, seg[a][1])
            a += 1
        if not (b & 1):
            ret_min = min(ret_min, seg[b][0])
            ret_max = max(ret_max, seg[b][1])
            b -= 1
        
        a >>= 1
        b >>= 1
    return [ret_min, ret_max]

if __name__ == '__main__':
    n, m = mis()
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [[float('inf'), 0] for _ in range(size)]

    for i in range(n):
        tmp = int(si())
        seg[(1 << height) + i] = [tmp, tmp]

    init()
    for _ in range(m):
        a, b = mis()
        print(*query(a, b))