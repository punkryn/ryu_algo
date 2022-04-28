# https://www.acmicpc.net/problem/19542
import sys
si = sys.stdin.readline

def DFS(x, prev, depth):
    global dist
    tmp = d
    for nxt in tree[x]:
        if nxt == prev: continue
        tmp = DFS(nxt, x, depth + 1)
        if tmp <= 0:
            dist.add(x)
    if tmp <= 0:
        dist.add(x)
    return tmp - 1

if __name__ == '__main__':
    n, s, d = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)

    dist = set()
    DFS(s, 0, 0)
    if dist:
        print((len(dist) - 1) * 2)
    else:
        print(0)