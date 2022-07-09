# https://www.acmicpc.net/problem/3013
import sys
from bisect import bisect_left, bisect_right
si = sys.stdin.readline

if __name__ == '__main__':
    n, b = map(int, si().split())
    a = list(map(int, si().split()))
    pos = a.index(b)
    idx = pos - 1
    l = []
    ans = 1
    while idx >= 0:
        if a[idx] > b:
            if l:
                l.append(l[-1] + 1)
            else:
                l.append(1)
        else:
            if l:
                l.append(l[-1] - 1)
            else:
                l.append(-1)
        idx -= 1
    
    r = []
    idx = pos + 1
    while idx < n:
        if a[idx] > b:
            if r:
                r.append(r[-1] + 1)
            else:
                r.append(1)
        else:
            if r:
                r.append(r[-1] - 1)
            else:
                r.append(-1)
        idx += 1
    ans += l.count(0) + r.count(0)
    r.sort()
    for i in l:
        if i == 0: continue
        ans += bisect_right(r, -i) - bisect_left(r, -i)
    print(ans)