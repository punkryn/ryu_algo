# https://www.acmicpc.net/problem/11505
import sys
import math
si = sys.stdin.readline
mis = lambda: map(int, si().split())
MOD = 1000000007

def init(l, r, idx):
    if l == r:
        seg[idx] = arr[l]
        return seg[idx]
    
    mid = (l + r) // 2
    ret = (init(l, mid, idx * 2) * init(mid + 1, r, idx * 2 + 1)) % MOD
    seg[idx] = ret
    return ret

def update(left, right, idx, upd, val):
    if right < upd or upd < left:
        return
    
    if right == left:
        seg[idx] = arr[left]
        if idx % 2 == 0:
            seg[idx // 2] = (seg[idx] * seg[idx + 1]) % MOD
        else:
            seg[idx // 2] = (seg[idx - 1] * seg[idx]) % MOD
        return
    
    mid = (left + right) // 2
    update(left, mid, idx * 2, upd, val)
    update(mid + 1, right, idx * 2 + 1, upd, val)

    if idx != 0:
        if idx % 2 == 0:
            seg[idx // 2] = (seg[idx] * seg[idx + 1]) % MOD
        else:
            seg[idx // 2] = (seg[idx - 1] * seg[idx]) % MOD

def query(left, right, idx, l, r):
    if right < l or r < left:
        return 1
    
    if l <= left and right <= r:
        return seg[idx]
    
    mid = (left + right) // 2
    return (query(left, mid, idx * 2, l, r) * query(mid + 1, right, idx * 2 + 1, l, r)) % MOD


if __name__ == '__main__':
    n, m, k = mis()
    arr = [0] + [int(si()) for _ in range(n)]
    seg = [0] * (1 << (math.ceil(math.log2(n) + 1)))
    init(1, n, 1)
    for _ in range(m + k):
        a, b, c = mis()
        if a == 1:
            arr[b] = c
            update(1, n, 1, b, c)
        else:
            print(query(1, n, 1, b, c))