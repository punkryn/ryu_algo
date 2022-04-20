# https://www.acmicpc.net/problem/22945
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    
    l, r = 0, n - 1
    ans = 0
    while l < r:
        if a[l] > a[r]:
            ans = max(ans, a[r] * (r - l - 1))
            r -= 1
        else:
            ans = max(ans, a[l] * (r - l - 1))
            l += 1
    print(ans)