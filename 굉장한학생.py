# https://www.acmicpc.net/problem/2336
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def update(a, b):
    idx = (1 << height) + a - 1
    seg[idx] = b
    while idx > 1:
        idx >>= 1
        seg[idx] = min(seg[idx << 1], seg[idx << 1 | 1])

def query(a, b):
    a += (1 << height) - 1
    b += (1 << height) - 1
    ret = float('inf')
    while a <= b:
        if a & 1:
            ret = min(ret, seg[a])
            a += 1
        if not (b & 1):
            ret = min(ret, seg[b])
            b -= 1
        a >>= 1
        b >>= 1
    return ret

if __name__ == '__main__':
    n = int(si())
    first = list(mis())
    second = list(mis())
    third = list(mis())
    rank = [[] for _ in range(n + 1)]
    for i in range(n):
        rank[first[i]].append((i + 1))
    for i in range(n):
        rank[second[i]].append((i + 1))
    for i in range(n):
        rank[third[i]].append((i + 1))
    rank.sort()
    
    height = ceil(log2(n))
    size = 1 << (height + 1)
    seg = [float('inf')] * size
    update(rank[1][1], rank[1][2])
    ans = 1
    for i in range(2, n + 1):
        if rank[i][1] == 1:
            ans += 1
        else:
            val = query(1, rank[i][1] - 1)
            if val >= rank[i][2]:
                ans += 1
            update(rank[i][1], rank[i][2])
    print(ans)