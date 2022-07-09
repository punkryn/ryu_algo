# https://www.acmicpc.net/problem/1275
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def init():
    for i in range(height - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            seg[j] = seg[j << 1] + seg[j << 1 | 1]

def update(a, b):
    idx = (1 << height) + a - 1
    seg[idx] = b
    while idx > 1:
        idx >>= 1
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1]

def query(x, y):
    x += (1 << height) - 1
    y += (1 << height) - 1
    ret = 0
    while x <= y:
        if x & 1:
            ret += seg[x]
            x += 1
        if not (y & 1):
            ret += seg[y]
            y -= 1
        x >>= 1
        y >>= 1
    return ret

if __name__ == '__main__':
    n, q = mis()
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [0] * size
    arr = list(mis())
    for i in range(n):
        seg[(1 << height) + i] = arr[i]
    init()

    for _ in range(q):
        x, y, a, b = mis()
        if x > y:
            x, y = y, x
        print(query(x, y))
        update(a, b)