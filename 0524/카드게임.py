# https://www.acmicpc.net/problem/16566
from sys import stdin
from bisect import bisect_left

si = stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    parent[x] = y

if __name__ == '__main__':
    n, m, k = map(int, si().split())
    cards = sorted(list(map(int, si().split())))
    ks = list(map(int, si().split()))
    parent = [i for i in range(n + 1)]
    for k in ks:
        idx = find_parent(bisect_left(cards, k + 1))
        print(cards[idx])
        union(idx, idx + 1)