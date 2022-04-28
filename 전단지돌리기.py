# https://www.acmicpc.net/problem/19542
import sys
si = sys.stdin.readline

def DFS(x, prev):
    global dist
    ret = d
    for nxt in tree[x]:
        if nxt == prev: continue
        tmp = DFS(nxt, x)
        if tmp > d:
            dist += 1
        ret += tmp
    return ret

if __name__ == '__main__':
    n, s, d = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)

    dist = 0    
    DFS(s, 0)
    print(dist * 2)