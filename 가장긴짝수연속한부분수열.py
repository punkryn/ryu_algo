# https://www.acmicpc.net/problem/22857
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = list(map(int, si().split()))

    cnt = 0
    r = -1
    ans = 0
    for l in range(n):
        while r + 1 < n and cnt < k + 1:
            r += 1
            if a[r] % 2 == 1:
                cnt += 1
            
        ans = max(ans, r - l - cnt + 1)
        
        if a[l] % 2 == 1:
            cnt -= 1
        
    print(ans)