# https://www.acmicpc.net/problem/15666

import sys
si = sys.stdin.readline

def go(depth, prev, cur):
    if depth == 0:
        print(*cur)
        return
    
    for i in range(prev, n):
        if i > 0 and a[i - 1] == a[i]: continue
        cur.append(a[i])
        go(depth - 1, i, cur)
        cur.pop()

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = sorted(list(map(int, si().split())))
    go(m, 0, [])