# https://www.acmicpc.net/problem/2670
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
  n = int(si())
  s = [float(si()) for _ in range(n)]
  pm = [1] * (n + 1)
  for i in range(1, n + 1):
    pm[i] = (pm[i - 1] if pm[i - 1] != 0 else 1) * s[i - 1]
  
  ans = 0
  div = 1
  for i in range(1, n + 1):
    if pm[i] == 0:
      div = 1
      continue
    if pm[i] < div:
      div = pm[i]
      ans = max(ans, pm[i])
      continue
    
    ans = max(ans, pm[i] / div)
  print(f'{ans:.3f}')