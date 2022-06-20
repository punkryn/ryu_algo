# https://www.acmicpc.net/problem/16564
import sys
si = sys.stdin.readline

def deter(mid):
    cur = k
    for i in range(n):
        if x[i] < mid:
            cur -= mid - x[i]
            if cur < 0:
                return False
    return True

if __name__ == '__main__':
    n, k = map(int, si().split())
    x = [int(si()) for _ in range(n)]

    ans = 0
    l, r = 1, int(1e9)
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)