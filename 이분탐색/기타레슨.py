# https://www.acmicpc.net/problem/2343
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
lectures = list(map(int, si().split()))

def deter(size):
    cur = 0
    cnt = 0
    for lecture in lectures:
        if lecture > size:
            return False
        cur += lecture
        if cur > size:
            cnt += 1
            cur = lecture
    
    if cur <= size:
        cnt += 1
    # print(cnt)
    return 0 < cnt <= m

l, r, ans = 1, 10000 * n, 0
while l <= r:
    mid = (l + r) // 2
    # print(l, r, mid)
    if deter(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)