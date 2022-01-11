# https://www.acmicpc.net/problem/17266
import sys
si = sys.stdin.readline
n = int(si())
m = int(si())
x = list(map(int, si().split()))

def deter(H):
    ran = 0
    for pos in x:
        if pos - H > ran:
            return False
        ran = pos + H
    return ran >= n

l, r, ans = 1, int(1e5), 0
while l <= r:
    mid = (l + r) // 2
    if deter(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)