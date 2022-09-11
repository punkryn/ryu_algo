# https://www.acmicpc.net/problem/22856
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

# def dfs(x):
#   global last, ans, vcnt
#   cnt = 0
#   if vcnt == n and x == last:
#     return

#   if tree[x][0] != -1 and not visited[tree[x][0]]:
#     vcnt += 1
#     visited[tree[x][0]] = True
#     cnt += 1
#     ans += 1
#     dfs(tree[x][0])
  
#   if tree[x][1] != -1 and not visited[tree[x][1]]:
#     vcnt += 1
#     visited[tree[x][1]] = True
#     cnt += 1
#     ans += 1
#     dfs(tree[x][1])
  
#   if cnt == 0:
#     ans += 1
#     dfs(parent[x])

def dfs(x):
  if ~tree[x][0] and not visited[tree[x][0]]:
    visited[tree[x][0]] = True
    return dfs(tree[x][0]) + 1
  
  if ~tree[x][1] and not visited[tree[x][1]]:
    visited[tree[x][1]] = True
    return dfs(tree[x][1]) + 1
  
  return dfs(parent[x]) + 1 if last ^ x else 0
  
if __name__ == '__main__':
  n = int(si())
  tree = [[-1, -1] for _ in range(n + 1)]
  parent = [-1] * (n + 1)
  for _ in range(n):
    a, b, c = mis()
    if b != -1:
      tree[a][0] = b
      parent[b] = a
    if c != -1:
      tree[a][1] = c
      parent[c] = a
  
  last = 1
  cur = 1
  while tree[cur][1] != -1:
    last = tree[cur][1]
    cur = tree[cur][1]

  # vcnt = 1
  visited = [False] * (n + 1)
  visited[1] = True
  # ans = 0
  # dfs(1)
  # print(ans)
  print(dfs(1))