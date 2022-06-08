# https://www.acmicpc.net/problem/16168
import sys
si = sys.stdin.readline

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
    v, e = map(int, si().split())
    edges = [0] * (v + 1)
    parent = [i for i in range(v + 1)]
    for _ in range(e):
        a, b = map(int, si().split())
        edges[a] += 1
        edges[b] += 1
        union(a, b)
    
    o, e = 0, 0
    prev = find_parent(1)
    for i in range(1, v + 1):
        cur = find_parent(i)
        if prev != cur:
            print('NO')
            exit()
        if edges[i] % 2 == 0:
            o += 1
        else:
            e += 1
        prev = cur
    
    if e == 0 or e == 2:
        print('YES')
    else:
        print('NO')