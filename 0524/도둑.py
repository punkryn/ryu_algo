# https://www.acmicpc.net/problem/13422
import sys
si = sys.stdin.readline

def main():
    n, m, k = map(int, si().split())
    a = list(map(int, si().split()))
    a += a

    r = 0
    ans = 0
    cnt = 0
    total = 0
    limit = n + m - 1
    for l in range(n):
        while r < limit and cnt < m:
            cnt += 1
            total += a[r]
            r += 1
        
        if total < k:
            ans += 1

        cnt -= 1
        total -= a[l]
        if n == m:
            break
    print(ans)

if __name__ == '__main__':
    for _ in range(int(si())):
        main()