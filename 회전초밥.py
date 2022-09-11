# https://www.acmicpc.net/problem/2531
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
  n, d, k, c = mis()
  belt = [int(si()) for _ in range(n)]
  belt = belt + belt
  
  r = -1
  cnt = 0
  ans = 0
  cur = dict()
  for l in range(n):
    while r < 2 * n and cnt < k:
      cnt += 1
      r += 1

      if belt[r] not in cur:
        cur[belt[r]] = 0
      cur[belt[r]] += 1
      
      if cnt == k:
        if c not in cur:
          cur[c] = 0
        cur[c] += 1
        ans = max(ans, len(cur))
        cur[c] -= 1
        if cur[c] == 0:
          del cur[c]
    
    cnt -= 1
    cur[belt[l]] -= 1
    if cur[belt[l]] == 0:
      del cur[belt[l]]
  
  print(ans)