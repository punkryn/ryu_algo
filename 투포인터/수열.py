# https://www.acmicpc.net/problem/2559
import sys
si = sys.stdin.readline
n, k = map(int, si().split())
temperature = list(map(int, si().split()))
total, cnt, r, ans = 0, 0, -1, -100 * n
for l in range(n - k + 1):
    while r + 1 < n and cnt < k:
        r += 1
        cnt += 1
        total += temperature[r]
    
    ans = max(ans, total)
    total -= temperature[l]
    cnt -= 1
print(ans)