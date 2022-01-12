# https://www.acmicpc.net/problem/15565
import sys
si = sys.stdin.readline
n, k = map(int, si().split())
toy = list(map(int, si().split()))

cnt = 0

r, ans = -1, n + 1
for l in range(n):
    while r + 1 < n and cnt < k:
        r += 1
        cnt += 1 if toy[r] == 1 else 0

    if cnt >= k:
        ans = min(ans, r - l + 1)

    cnt -= 1 if toy[l] == 1 else 0

if ans == n + 1:
    ans = -1
print(ans)