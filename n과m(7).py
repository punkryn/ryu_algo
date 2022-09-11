# https://www.acmicpc.net/problem/15656
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(depth, cur=[]):
    if depth == m:
        print(*cur)
        return
    
    for i in range(n):
        cur.append(a[i])
        go(depth + 1, cur)
        cur.pop()

if __name__ == '__main__':
    n, m = mis()
    a = sorted(mis())
    go(0)