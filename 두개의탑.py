# https://www.acmicpc.net/problem/2118
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    p = [int(si()) for _ in range(n)]
    total = sum(p)
    p += p

    r = 0
    ans = 0
    cur = 0
    comp = 0
    for l in range(n):
        while r < n * 2 and r - l < n and cur <= total - cur:
            cur += p[r]

            r += 1
            comp = max(comp, min(cur, total - cur))

        ans = max(ans, comp)
        cur -= p[l]
    print(ans)