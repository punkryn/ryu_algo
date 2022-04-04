# https://www.acmicpc.net/problem/15810
import sys
si = sys.stdin.readline

def deter(mid):
    cnt = 0
    for v in a:
        cnt += mid // v
    return cnt >= m

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = list(map(int, si().split()))
    l, r = 1, int(1e12)
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans)