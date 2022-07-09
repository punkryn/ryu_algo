# https://www.acmicpc.net/problem/3653
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

def query(a, b):
    a += (1 << height) - 1
    b += (1 << height) - 1
    ret = 0
    while a <= b:
        if a & 1:
            ret += seg[a]
            a += 1
        if not (b & 1):
            ret += seg[b]
            b -= 1
        a >>= 1
        b >>= 1
    return ret

if __name__ == '__main__':
    for _ in range(int(si())):
        n, m = mis()
        arr = list(mis())
        height = ceil(log2(n + m))
        size = 1 << (height + 1)
        seg = [0] * size
        pos = [i for i in range(n + 1)]
        pos = [0] + pos[1::-1]
        pos.pop()
        for i in range(n):
            seg[(1 << height) + i] = 1
        init()
        for i in range(m):
            print(query(pos[arr[i]] + 1, n + m), end=' ')
            update(n + i + 1, 1)
            update(pos[arr[i]], 0)
            pos[arr[i]] = n + i + 1
            
        print()