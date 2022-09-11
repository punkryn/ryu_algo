import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
  n, m = mis()
  a = [list(mis()) for _ in range(m)]
  bonus = sorted(list(mis()), reverse=True)

  indegree = [0] * (n + 1)
  graph = [[] for _ in range(n + 1)]
  for x, y in a:
    indegree[y] += 1
    graph[x].append(y)
  
  q = deque()
  ans = [0] * (n + 1)
  pos = 0
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)
      ans[i] = bonus[pos]
      pos += 1

  while q:
    print(ans[1:])
    cur = q.popleft()

    for nxt in graph[cur]:
      indegree[nxt] -= 1

      if indegree[nxt] == 0:
        q.append(nxt)
        ans[nxt] = bonus[pos]
        pos += 1
  
  print(*ans[1:])