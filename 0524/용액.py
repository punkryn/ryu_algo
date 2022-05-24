# https://www.acmicpc.net/problem/2467
import sys
from bisect import bisect_left

si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))

    l, r = 0, n - 1
    b = int(1e11)
    ans = [0, 0]
    while l < r:
        tmp = a[l] + a[r]
        if abs(tmp) < b:
            b = abs(tmp)
            ans[0], ans[1] = a[l], a[r]
        
        if tmp > 0:
            r -= 1
        else:
            l += 1
    
    print(*sorted(ans))