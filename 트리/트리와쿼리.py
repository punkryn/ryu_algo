# https://www.acmicpc.net/problem/15681
import sys
from collections import deque
sys.setrecursionlimit(1000000)
si = sys.stdin.readline

def main():
    n, r, q = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, si().split())
        tree[u].append(v)
        tree[v].append(u)
    
    parents = [0] * (n + 1)

    def dfs(x, par):
        cnt = 1
        for nxt in tree[x]:
            if nxt == par: continue
            cnt += dfs(nxt, x)
        parents[x] = cnt
        return cnt

    queries = [int(si()) for _ in range(q)]
    
    dfs(r, -1)
    for u in queries:
        par = parents[u]
        print(par)

if __name__ == '__main__':
    main()