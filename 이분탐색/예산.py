# https://www.acmicpc.net/problem/2512
import sys
si = sys.stdin.readline
n = int(si())
req = list(map(int, si().split()))
m = int(si())

def deter(M):
    total = 0
    for r in req:
        if r >= M:
            total += M
        else:
            total += r
    return total <= m

if sum(req) <= m:
    print(max(req))
else:
    start = 1
    end = int(1e9)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if deter(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)