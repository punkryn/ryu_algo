# https://www.acmicpc.net/problem/12912
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def dfs(x, prev, diameter, start, rad):
  if x != start[0] and len(tree[x]) == 1:
    if rad[0] < diameter:
      rad[0] = diameter
      start[0] = x
    return
  
  for nxt in tree[x]:
    if nxt == prev: continue
    dfs(nxt, x, diameter + tree[x][nxt], start, rad)

if __name__ == '__main__':
  n = int(si())
  tree = [dict() for _ in range(n)]
  edges = set()
  for _ in range(n - 1):
    u, v, c = mis()
    tree[u][v] = c
    tree[v][u] = c
    edges.add((u, v, c))
  
  ans = 0
  for u, v, c in edges:
    del tree[u][v]
    del tree[v][u]

    s1 = [u]
    r1 = [0]
    dfs(u, -1, 0, s1, r1)
    dfs(s1[0], -1, 0, s1, r1)

    s2 = [v]
    r2 = [0]
    dfs(v, -1, 0, s2, r2)
    dfs(s2[0], -1, 0, s2, r2)

    ans = max(ans, r1[0] + r2[0] + c)
    tree[u][v] = c
    tree[v][u] = c
  
  print(ans)