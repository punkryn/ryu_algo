# https://www.acmicpc.net/problem/13702
import sys
si = sys.stdin.readline
n, k = map(int, si().split())
capacity = [int(si()) for _ in range(n)]

def deter(capa):
    total = 0
    for c in capacity:
        total += (c // capa)
    return total >= k

l, r, ans = 0, 1 << 31, 0
while l <= r:
    mid = (l + r) // 2
    if deter(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)