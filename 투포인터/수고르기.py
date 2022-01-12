# https://www.acmicpc.net/problem/2230
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
A = [int(si()) for _ in range(n)]
A.sort()
r = 0
ans = 2 * int(1e9)
for l in range(n):
    while r < n and abs(A[r] - A[l]) < m:
        r += 1
    if r == n:
        r -= 1
    # print(l, r)
    if abs(A[r] - A[l]) >= m:
        ans = min(ans, abs(A[r] - A[l]))
print(ans)