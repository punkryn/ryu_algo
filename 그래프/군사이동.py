# https://www.acmicpc.net/problem/11085
import sys
si = sys.stdin.readline

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    p, w = map(int, si().split())
    c, v = map(int, si().split())
    
    graph = [list(map(int, si().split())) for _ in range(w)]
    graph.sort(key=lambda x: x[2], reverse=True)
    parent = [i for i in range(p)]

    for g in graph:
        u_, v_, w_ = g
        union(parent, u_, v_)

        if find(parent, c) == find(parent, v):
            print(w_)
            break