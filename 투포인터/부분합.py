# https://www.acmicpc.net/problem/1806
import sys
si = sys.stdin.readline
n, s = map(int, si().split())
seq = list(map(int, si().split()))

total, r, ans = 0, -1, int(1e5)
for i in range(n):
    while total < s and r + 1 < n:
        r += 1
        total += seq[r]
    # print(total, i, r)
    if total >= s:
        ans = min(ans, r - i + 1)
    total -= seq[i]

if ans == int(1e5):
    print(0)
else:
    print(ans)