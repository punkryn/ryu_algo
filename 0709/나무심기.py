# https://www.acmicpc.net/problem/1280
import sys
from math import log2, ceil
si = sys.stdin.readline
mis = lambda: map(int, si().split())

MAX = 200000
MOD = int(1e9) + 7

def cnt_update(a):
    idx = (1 << height) + a - 1
    cnt[idx] += 1
    while idx > 1:
        idx >>= 1
        cnt[idx] = cnt[idx << 1] + cnt[idx << 1 | 1]

def sum_update(a, b):
    idx = (1 << height) + a - 1
    SUM[idx] += b
    while idx > 1:
        idx >>= 1
        SUM[idx] = SUM[idx << 1] + SUM[idx << 1 | 1]
        
def cnt_query(a, b):
    a += (1 << height) - 1
    b += (1 << height) - 1
    ret = 0
    while a <= b:
        if a & 1:
            ret += cnt[a]
            a += 1
        if not (b & 1):
            ret += cnt[b]
            b -= 1
        a >>= 1
        b >>= 1
    return ret

def sum_query(a, b):
    a += (1 << height) - 1
    b += (1 << height) - 1
    ret = 0
    while a <= b:
        if a & 1:
            ret += SUM[a]
            a += 1
        if not (b & 1):
            ret += SUM[b]
            b -= 1
        a >>= 1
        b >>= 1
    return ret

if __name__ == '__main__':
    n = int(si())
    height = ceil(log2(MAX))
    size = 1 << (height + 1)
    cnt = [0] * size
    SUM = [0] * size
    
    ans = 1
    for _ in range(n):
        tmp = int(si())
        cnt_update(tmp)
        sum_update(tmp, tmp)
        if _ == 0:
            continue
        left = cnt_query(0, tmp - 1) * tmp - sum_query(0, tmp - 1)
        right = sum_query(tmp + 1, MAX - 1) - cnt_query(tmp + 1, MAX - 1) * tmp
        ans = ans * (left + right) % MOD
    print(ans % MOD)