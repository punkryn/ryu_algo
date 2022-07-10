# https://www.acmicpc.net/problem/2243
import sys
from math import ceil, log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())

MAX = int(1e6)

def update(left, right, idx, a, b):
    if right < a or a < left:
        return
    seg[idx] += b
    if left == right:
        return
    
    mid = (left + right) // 2
    update(left, mid, idx * 2, a, b)
    update(mid + 1, right, idx * 2 + 1, a, b)

def bs(left, right, idx, a):
    if left == right:
        return left
    
    mid = (left + right) // 2
    if seg[idx * 2] >= a:
        return bs(left, mid, idx * 2, a)
    return bs(mid + 1, right, idx * 2 + 1, a - seg[idx * 2])

if __name__ == '__main__':
    n = int(si())
    height = ceil(log2(MAX))
    size = 1 << (height + 1)
    seg = [0] * size
    for i in range(n):
        op = list(mis())
        if len(op) == 3:
            a, b = op[1], op[2]
            update(1, MAX, 1, a, b)
        else:
            a = op[1]
            pos = bs(1, MAX, 1, a)
            print(pos)
            update(1, MAX, 1, pos, -1)