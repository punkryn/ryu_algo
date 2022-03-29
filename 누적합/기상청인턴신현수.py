# https://www.acmicpc.net/problem/2435
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = list(map(int, si().split()))

    j = 0
    cnt = 0
    total = 0
    ans = -100000
    for i in range(n):
        while cnt < k and j < n:
            total += a[j]
            j += 1
            cnt += 1
            if cnt == k:
                ans = max(ans, total)
        
        cnt -= 1
        total -= a[i]
    print(ans)