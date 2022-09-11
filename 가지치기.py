# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=836&sca=5050
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = int(1e9)

def dfs(x, prev, root):
  if x != root and len(tree[x]) == 1:
    return dp[x]
  
  dp[x] = 0
  for nxt, cost in tree[x]:
    if nxt == prev: continue
    dfs(nxt, x, root)
    dp[x] += min(cost, dp[nxt])
  return dp[x]

if __name__ == '__main__':
  while True:
    n, r = mis()
    if n == 0 and r == 0:
      break
    
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
      u, v, w = mis()
      tree[u].append((v, w))
      tree[v].append((u, w))
    
    dp = [INF] * (n + 1)
    print(dfs(r, -1, r))