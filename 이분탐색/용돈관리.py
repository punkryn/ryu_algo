# https://www.acmicpc.net/problem/6236
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
money = [int(si()) for _ in range(n)]

def deter(draw):
    cur = 0
    cnt = 1
    for mo in money:
        if mo + cur > draw:
            cur = mo
            cnt += 1
        else:
            cur += mo
    return cnt <= m

l, r, ans = max(money), int(1e9), 0
while l <= r:
    mid = (l + r)//2
    if deter(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)