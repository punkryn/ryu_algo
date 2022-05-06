# https://www.acmicpc.net/problem/16401
import sys
si = sys.stdin.readline

def deter(mid):
    if mid == 0:
        return False
    cnt = 0
    for i in range(n):
        cnt += L[i] // mid
    return cnt >= m

if __name__ == "__main__":
    m, n = map(int, si().split())
    L = list(map(int, si().split()))
    l, r = 0, max(L)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if deter(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)