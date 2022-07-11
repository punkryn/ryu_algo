# https://www.acmicpc.net/problem/10999
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def init():
    for i in range(height - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            seg[j] = seg[j << 1] + seg[j << 1 | 1]

def propagate(idx, l, r):
    if lazy[idx]:
        if idx < (1 << height):
            lazy[idx << 1] += lazy[idx]
            lazy[idx << 1 | 1] += lazy[idx]
        seg[idx] += lazy[idx] * (r - l)
        lazy[idx] = 0

def update(left, right, idx, b, c, d):
    propagate(idx, left, right)
    if right <= b or c <= left:
        return
    
    if b <= left and right <= c:
        lazy[idx] += d
        propagate(idx, left, right)
        return
    
    mid = (left + right) // 2
    update(left, mid, idx * 2, b, c, d)
    update(mid, right, idx * 2 + 1, b, c, d)
    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1]

def query(left, right, idx, b, c):
    propagate(idx, left, right)
    if right <= b or c <= left:
        return 0
    if b <= left and right <= c:
        return seg[idx]
    
    mid = (left + right) // 2
    return query(left, mid, idx << 1, b, c) + query(mid, right, idx << 1 | 1, b, c)

if __name__ == '__main__':
    n, m, k = mis()
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [0] * size
    lazy = [0] * size
    for i in range(n):
        seg[(1 << height) + i] = int(si())
    init()

    for i in range(m + k):
        a, *op = mis()
        if a == 1:
            b, c, d = op
            update(0, 1 << height, 1, b - 1, c, d)
        else:
            b, c = op
            print(query(0, 1 << height, 1, b - 1, c))