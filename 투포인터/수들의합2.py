# https://www.acmicpc.net/problem/2003
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
A = list(map(int, si().split()))

total, r, ans = 0, -1, 0
for l in range(n):
    while r + 1 < n and total + A[r + 1] <= m:
        r += 1
        total += A[r]
    # print(total)
    if total == m:
        ans += 1
    
    total -= A[l]
print(ans)