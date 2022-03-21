# https://www.acmicpc.net/problem/2900
import sys
import math
from collections import defaultdict
si = sys.stdin.readline

def sum(idx, tree):
    ans = 0
    while idx > 0:
        ans += tree[idx]
        idx -= (idx & -idx)
    return ans

def update(idx, num, tree):
    while idx < len(tree):
        tree[idx] += num
        idx += (idx & -idx)

def main():
    n, k = map(int, si().split())
    x = list(map(int, si().split()))
    q = int(si())
    checks = [list(map(int, si().split())) for _ in range(q)]

    tree = [0] * (n + 1)
    m = defaultdict(int)
    for xi in x:
        m[xi] += 1
    
    for key in m:
        for i in range(1, n + 1, key):
            update(i, m[key], tree)
    
    for query in checks:
        l, r = query
        print(sum(r + 1, tree) - sum(l, tree))

if __name__ == '__main__':
    main()