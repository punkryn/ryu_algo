# https://www.acmicpc.net/problem/3273
import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
x = int(si())
a.sort()
l, r, total, ans = 0, n-1, 0, 0
# print(a)
while l < r:
    if a[l] + a[r] == x:
        ans += 1

    if a[l] + a[r] > x:
        r -= 1
    else:
        l += 1

print(ans)