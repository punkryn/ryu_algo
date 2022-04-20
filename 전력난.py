# https://www.acmicpc.net/problem/6497
import sys
si = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def main():
    n, m = map(int, si().split())
    if n == 0 and m == 0: exit()
    roads = [list(map(int, si().split())) for _ in range(m)]
    parent = [i for i in range(n + 1)]
    roads.sort(key=lambda x: x[2])

    mst = 0
    total = 0
    for x, y, z in roads:
        total += z
        if find_parent(parent, x) != find_parent(parent, y):
            union(parent, x, y)
            mst += z
    print(total - mst)

if __name__ == '__main__':
    while True:
        main()