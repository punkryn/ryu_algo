# https://www.acmicpc.net/problem/11505
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

MOD = int(1e9) + 7

def init():
    for i in range(height - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            seg[j] = (seg[j << 1] * seg[j << 1 | 1]) % MOD

def update(b, c):
    idx = (1 << height) + b - 1
    seg[idx] = c
    while idx > 1:
        idx //= 2
        seg[idx] = (seg[idx << 1] * seg[idx << 1 | 1]) % MOD

def query(b, c):
    res = 1
    b += (1 << height ) - 1
    c += (1 << height ) - 1
    while b <= c:
        if b & 1:
            res = res * seg[b] % MOD
            b += 1
        if not (c & 1):
            res = res * seg[c] % MOD
            c -= 1
        b >>= 1
        c >>= 1
    return res

if __name__ == '__main__':
    n, m, k = mis()
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [1] * size
    for i in range(n):
        seg[(1 << height) + i] = int(si())
    
    init()
    for _ in range(m + k):
        a, b, c = mis()
        if a == 1:
            update(b, c)
        else:
            print(query(b, c))