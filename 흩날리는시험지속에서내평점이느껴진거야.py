# https://www.acmicpc.net/problem/17951
import sys
si = sys.stdin.readline

def deter(mid):
    cnt = 0
    cur = 0
    for a in x:
        cur += a
        if cur >= mid:
            cnt += 1
            cur = 0
    
    if cur != 0:
        cnt += 1
    else:
        if cnt >= k:
            return True
    if cnt > k:
        return True
    else:
        if cur >= mid:
            return True
        else:
            return False

if __name__ == '__main__':
    n, k = map(int, si().split())
    x = list(map(int, si().split()))
    l, r = 0, 20 * n
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)