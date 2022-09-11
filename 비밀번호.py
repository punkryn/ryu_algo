# https://www.acmicpc.net/problem/13908
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(depth, cur=[]):
    global ans
    if depth == n:
        tmp = a[:]
        for c in cur:
            tmp[c] = 0
        
        if sum(tmp) == 0:
            ans += 1
        return
    
    for i in range(10):
        cur.append(i)
        go(depth + 1, cur)
        cur.pop()

if __name__ == '__main__':
    n, m = mis()
    a = [0] * 10
    if m != 0:
        b = list(mis())
        for i in b:
            a[i] = 1
    
    ans = 0
    go(0)
    print(ans)