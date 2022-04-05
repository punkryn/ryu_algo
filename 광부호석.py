# https://www.acmicpc.net/problem/21279
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, c = map(int, si().split())
    a = sorted([list(map(int, si().split())) for _ in range(n)])
    b = sorted(a, key=lambda x: x[1])

    ps = []
    r = -1
    cnt = 0
    total = 0
    ans = 0
    h, v = 0, 0
    for i in range(n - c + 1):
        h2, v2 = 0, 0
        while r + 1 < n and cnt < c:
            r += 1
            cnt += 1
            total += a[r][2]
            
            if h < a[r][1]:
                tmp = h
                tmp2 = v
                h = a[r][1]
                v = a[r][2]
                if tmp > h2:
                    h2 = tmp
                    v2 = tmp2
            else:
                if h2 < a[r][1]:
                    h2 = a[r][1]
                    v2 = a[r][2]
        
        ans = max(ans, total)
        cnt -= 1
        total -= v
        h = h2
        v = v2
    print(ans)