# https://www.acmicpc.net/problem/2230
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, m = mis()
    a = sorted([int(si()) for _ in range(n)])
    
    r = 0
    ans = float('inf')
    for l in range(n):
        while r < n and abs(a[r] - a[l]) < m:
            r += 1
        
        if r == n: r -= 1
        diff = abs(a[r] - a[l])
        if diff >= m:
            ans = min(ans, diff)
    print(ans)