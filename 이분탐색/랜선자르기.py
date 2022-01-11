# https://www.acmicpc.net/problem/1654
import sys
k, n = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]

start = 0
end = 1 << 32

def deter(M):
    cnt = 0
    for cable in cables:
        cnt += (cable // M)
    return cnt >= n

res = 1
while start <= end:
    mid = (start + end) // 2
    if deter(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)