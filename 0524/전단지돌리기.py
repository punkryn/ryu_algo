# https://www.acmicpc.net/problem/19542
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def DFS(x, prev):
    global dist
    
    if len(tree[x]) == 1 and prev != 0:
        return d

    minv = int(1e9)
    for nxt in tree[x]:
        if nxt == prev: continue
        tmp = DFS(nxt, x)
        minv = min(minv, tmp)
        if tmp > 0:
            dist -= 1
    return minv - 1

if __name__ == '__main__':
    n, s, d = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)
    dist = n
    DFS(s, 0)
    print((dist - 1) * 2)