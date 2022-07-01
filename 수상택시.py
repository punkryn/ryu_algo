# https://www.acmicpc.net/problem/2836
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    if n == 0:
        print(m)
        exit()
    pos = []
    for _ in range(n):
        a, b = map(int, si().split())
        if a > b:
            pos.append((a, b))
    pos.sort(key=lambda x: -x[0])
    l, r = -1, -1
    ans = m
    rev = []
    for x, y in pos:
        if l == -1 and r == -1:
            l = x
            r = y
            continue
        if x >= r:
            r = min(r, y)
        else:
            ans += (l - r) * 2
            l = x
            r = y
    ans += (l - r) * 2
    print(ans)