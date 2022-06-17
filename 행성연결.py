# https://www.acmicpc.net/problem/16398
import sys
si = sys.stdin.readline

def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

if __name__ == '__main__':
    n = int(si())
    costs = [list(map(int, si().split())) for _ in range(n)]
    parents = [i for i in range(n)]
    edges = sorted([(costs[i][j], i, j) for i in range(n) for j in range(n) if i != j])
    ans = 0
    for cost, x, y in edges:
        if find_parent(x) != find_parent(y):
            ans += cost
            union(x, y)
    print(ans)