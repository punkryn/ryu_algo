# https://www.acmicpc.net/problem/17073
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def dfs(x, prev):
    global total, cnt
    if len(tree[x]) == 1:
        total += val[x]
        cnt += 1
        return
    
    m = val[x] / (len(tree[x]) - 1)
    for nxt in tree[x]:
        if nxt == prev: continue
        if nxt == -1: continue
        val[nxt] = m
        dfs(nxt, x)

if __name__ == '__main__':
    n, w = mis()
    tree = [[] for _ in range(n + 1)]
    tree[1].append(-1)
    for _ in range(n - 1):
        u, v = mis()
        tree[u].append(v)
        tree[v].append(u)
    
    val = [0] * (n + 1)
    val[1] = w
    total = 0
    cnt = 0
    dfs(1, -1)
    print(total / cnt)