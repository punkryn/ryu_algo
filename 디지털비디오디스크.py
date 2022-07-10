# https://www.acmicpc.net/problem/9345
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def init():
    for i in range(height - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            seg[j][0] = min(seg[j << 1][0], seg[j << 1 | 1][0])
            seg[j][1] = max(seg[j << 1][1], seg[j << 1 | 1][1])

def update(a, b):
    idx = (1 << height) + a
    seg[idx][0] = b
    seg[idx][1] = b
    while idx > 1:
        idx >>= 1
        seg[idx][0] = min(seg[idx << 1][0], seg[idx << 1 | 1][0])
        seg[idx][1] = max(seg[idx << 1][1], seg[idx << 1 | 1][1])

def query(a, b):
    a += (1 << height)
    b += (1 << height)
    ret = [n, 0]
    while a <= b:
        if a & 1:
            ret[0] = min(ret[0], seg[a][0])
            ret[1] = max(ret[1], seg[a][1])
            a += 1
        if not (b & 1):
            ret[0] = min(ret[0], seg[b][0])
            ret[1] = max(ret[1], seg[b][1])
            b -= 1
        a >>= 1
        b >>= 1
    return ret

if __name__ == '__main__':
    for _ in range(int(si())):
        n, k = mis()
        pos = [i for i in range(n)]
        height = ceil(log2(n))
        size = 1 << (height + 1)
        seg = [[n, 0] for _ in range(size)]
        for i in range(n):
            seg[(1 << height) + i] = [i, i]
        init()
        
        for _ in range(k):
            q, a, b = mis()
            if q == 1:
                print('YES' if query(a, b) == [a, b] else 'NO')
            else:
                update(pos[a], b)
                update(pos[b], a)
                pos[a], pos[b] = pos[b], pos[a]