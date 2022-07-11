# https://www.acmicpc.net/problem/5419
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def query(a, b):
    a += (1 << height)
    b += (1 << height)
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

def update(a):
    idx = (1 << height) + a
    seg[idx] += 1
    while idx > 1:
        idx >>= 1
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1]
    
if __name__ == '__main__':
    for _ in range(int(si())):
        n = int(si())
        coord = sorted([list(mis()) for _ in range(n)], key=lambda x: x[1])
        newY = [0] * n
        order = 0
        for i in range(n):
            if i > 0 and coord[i][1] != coord[i - 1][1]:
                order += 1
            newY[i] = order
        
        for i in range(n):
            coord[i][1] = newY[i]
        
        coord.sort(key=lambda x: (x[0], -x[1]))
        
        height = ceil(log2(n))
        size = 1 << (height + 1)
        seg = [0] * size

        ans = 0
        for i in range(n):
            ans += query(coord[i][1], n - 1)
            update(coord[i][1])
        print(ans)