# https://www.acmicpc.net/problem/15900
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline

def main():
    n = int(si())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, si().split())
        edges[a].append(b)
        edges[b].append(a)
    
    leaf = [0] * (n + 1)
    def dfs(x, par, depth):
        if x != 1 and len(edges[x]) == 1:
            leaf[x] = depth
        
        for nxt in edges[x]:
            if nxt == par: continue
            dfs(nxt, x, depth + 1)
            leaf[x] += leaf[nxt]
    
    dfs(1, -1, 0)
    if leaf[1] % 2 == 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()