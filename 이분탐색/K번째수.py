# https://www.acmicpc.net/problem/1300
import sys
import math
si = sys.stdin.readline
n = int(si())
k = int(si())

def deter(cand):
    total = 0
    for i in range(1, n + 1):
        total += min(n, cand // i)
    # print('total', total)
    return total >= k

l, r, ans = 1, n * n, 0
while l <= r:
    mid = (l + r) // 2
    # print(l, r, mid)
    if deter(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)