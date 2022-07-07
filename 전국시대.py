# https://www.acmicpc.net/problem/15809
import sys
si = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    parent[y] = x
    return x < y

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = [0] + [int(si()) for _ in range(n)]
    
    parent = [i for i in range(n + 1)]

    for _ in range(m):
        o, p, q = map(int, si().split())
        if o == 1:
            fp = find_parent(p)
            fq = find_parent(q)
            union(p, q)
            a[fp] += a[fq]
        else:
            fp = find_parent(p)
            fq = find_parent(q)
            if a[fp] < a[fq]:
                union(fq, fp)
                a[fq] = a[fq] - a[fp]
            elif a[fp] > a[fq]:
                union(fp, fq)
                a[fp] = a[fp] - a[fq]
            else:
                a[fp] = a[fq] = 0
    ans = set()
    for i in range(1, n + 1):
        fi = find_parent(i)
        if a[fi]:
            ans.add(fi)
    print(len(ans))
    print(*sorted([a[key] for key in ans]))