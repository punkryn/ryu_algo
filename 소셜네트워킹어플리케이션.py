# https://www.acmicpc.net/problem/7511
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    for _ in range(1, int(si()) + 1):
        print(f'Scenario {_}:')
        n = int(si())
        k = int(si())
        parent = [i for i in range(n)] 
        for _ in range(k):
            a, b = mis()
            if find_parent(a) != find_parent(b):
                union(a, b)
        m = int(si())
        for i in range(m):
            u, v = mis()
            print(1 if find_parent(u) == find_parent(v) else 0)
        print()