# https://www.acmicpc.net/problem/13397
import sys
si = sys.stdin.readline

def deter(mid):
    minv = int(1e6)
    maxv = 0
    cnt = 1
    for i in range(n):
        minv = min(minv, a[i])
        maxv = max(maxv, a[i])
        if maxv - minv > mid:
            cnt += 1
            minv = a[i]
            maxv = a[i]
    return cnt <= m

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = list(map(int, si().split()))

    l, r = 0, 10000
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans)