# https://www.acmicpc.net/problem/12837
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def update(p, x):
    idx = (1 << height) + p - 1
    seg[idx] += x
    while idx > 1:
        idx >>= 1
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1]

def query(p, q):
    p += (1 << height) - 1
    q += (1 << height) - 1
    ret = 0
    while p <= q:
        if p & 1:
            ret += seg[p]
            p += 1
        if not (q & 1):
            ret += seg[q]
            q -= 1
        p >>= 1
        q >>= 1
    return ret

if __name__ == '__main__':
    n, q = mis()
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [0] * size
    for _ in range(q):
        op, p, q = mis()
        if op == 1:
            update(p, q)
        else:
            print(query(p, q))