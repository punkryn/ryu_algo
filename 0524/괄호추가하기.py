# https://www.acmicpc.net/problem/16637
import sys
import copy
si = sys.stdin.readline

def calc(base, op, nxt):
    if op == '+': return base + nxt
    elif op == '-': return base - nxt
    else: return base * nxt

def select(depth, cur):
    global ans
    if depth >= n:
        ans = max(ans, cur)
        return
    
    op = '+' if depth == 0 else f[depth - 1]
    if depth + 2 < n:
        b = calc(int(f[depth]), f[depth + 1], int(f[depth + 2]))
        select(depth + 4, calc(cur, op, b))
    select(depth + 2, calc(cur, op, int(f[depth])))

if __name__ == '__main__':
    n = int(si())
    f = si().rstrip()
    
    ans = -int(1e10)
    select(0, 0)
    print(ans)