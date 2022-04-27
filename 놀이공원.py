# https://www.acmicpc.net/problem/1561
import sys

si = sys.stdin.readline

def deter(mid):
    total = 0
    for i in a:
        total += (mid // i + 1)
    return total >= n

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = list(map(int, si().split()))
    
    if n <= m:
        print(n)
        exit()

    l, r = 0, int(3e11)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    prev = ans - 1
    total = 0
    for i in a:
        total += (prev // i + 1)
    for i in range(len(a)):
        if ans % a[i] == 0:
            total += 1
            if total == n:
                print(i + 1)
                break