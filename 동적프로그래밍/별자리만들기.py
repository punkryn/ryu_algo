# https://www.acmicpc.net/problem/4386
import sys
import math
si = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n = int(si())
    coordinate = [list(map(float, si().split())) for _ in range(n)]
    lines = []
    for i in range(n - 1):
        for j in range(1, n):
            x1, y1 = coordinate[i]
            x2, y2 = coordinate[j]
            length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            lines.append((length, i, j))
    
    parent = [i for i in range(n)]
    lines.sort()

    ans = 0
    for line in lines:
        l, x, y = line
        if find_parent(x) != find_parent(y):
            union(x, y)
            ans += l
    print(f'{ans:.2f}')