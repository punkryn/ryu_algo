# https://www.acmicpc.net/problem/1208
import sys
si = sys.stdin.readline

def left(depth, cur):
    if depth == n // 2:
        if cur not in init:
            init[cur] = 0
        init[cur] += 1
        return
    
    left(depth + 1, cur)
    left(depth + 1, cur + a[depth])

def right(depth, cur):
    global ans
    if depth == n:
        if s - cur in init:

            ans += init[s - cur]
        return
    
    right(depth + 1, cur)
    right(depth + 1, cur + a[depth])

if __name__ == '__main__':
    n, s = map(int, si().split())
    a = list(map(int, si().split()))
    
    init = dict()    
    ans = 0
    
    left(0, 0)
    right(n // 2, 0)
    if s == 0: ans -= 1
    print(ans)