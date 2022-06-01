# https://www.acmicpc.net/problem/15657
import sys
si = sys.stdin.readline

def go(depth, cur=[], start=0):
    if depth == m:
        print(*cur)
        return
    
    for i in range(start, n):
        cur.append(a[i])
        go(depth + 1, cur, i)
        cur.pop()

if __name__ == '__main__':
    n, m = map(int, si().split())
    a = sorted(list(map(int, si().split())))
    go(0)