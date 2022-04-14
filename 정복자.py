# https://www.acmicpc.net/problem/14950
import sys
import heapq
si = sys.stdin.readline

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

if __name__ == "__main__":
    n, m, t = map(int, si().split())
    
    parent = [i for i in range(n + 1)]
    graph = [list(map(int, si().split())) for _ in range(m)]
    graph.sort(key=lambda x: x[2])
    cnt = 0
    ans = 0
    for a, b, c in graph:
        if find_parent(a) != find_parent(b):
            union(a, b)
            ans += c + t * cnt
            cnt += 1
    print(ans)