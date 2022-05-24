# https://www.acmicpc.net/problem/16724
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
    zone = [si().strip() for _ in range(n)]
    
    parent = [i for i in range(n * m)]

    d = {
        'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)
    }

    for i in range(n):
        for j in range(m):
            w = zone[i][j]
            ni = i + d[w][0]
            nj = j + d[w][1]
            cur = i * m + j
            nxt = ni * m + nj
            union(cur, nxt)
    
    ans = set()
    for i in range(n * m):
        ans.add(find_parent(i))
    print(len(ans))