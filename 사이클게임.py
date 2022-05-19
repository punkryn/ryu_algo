# https://www.acmicpc.net/problem/20040
from sys import stdin
si = stdin.readline

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
    n, m = map(int, si().split())

    parent = [i for i in range(n)]
    ans = 0
    flag = True
    for _ in range(m):
        a, b = map(int, si().split())
        if find_parent(a) != find_parent(b):
            union(a, b)
        else:
            print(_ + 1)
            exit()
    print(ans)