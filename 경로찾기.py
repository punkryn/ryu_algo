# https://www.acmicpc.net/problem/2479
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
  n, k = mis()
  codes = [si().strip() for _ in range(n)]
  A, B = mis()
  A, B = A - 1, B - 1

  graph = [[] for _ in range(n)]
  # 해밍 거리
  for i in range(n - 1):
    for j in range(i + 1, n):
      cnt = 0
      for l in range(k):
        if codes[i][l] != codes[j][l]:
          cnt += 1
      
      if cnt == 1:
        graph[i].append(j)
        graph[j].append(i)
  
  q = deque([A])
  visited = [-1] * n
  visited[A] = 0

  prev = [-1] * n
  while q:
    cur = q.popleft()

    if cur == B:
      break

    for nxt in graph[cur]:
      if visited[nxt] != -1: continue
      
      visited[nxt] = visited[cur] + 1
      q.append(nxt)
      prev[nxt] = cur
  
  ans = []
  while prev[B] != -1:
    ans.append(B)
    B = prev[B]
  ans.append(B)

  if len(ans) != 1:
    print(*[e + 1 for e in ans[::-1]])
  else:
    print(-1)