# https://www.acmicpc.net/problem/17124
import sys
from bisect import bisect
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    for _ in range(int(si())):
        n, m = mis()
        a = list(mis())
        b = sorted(mis())
        c = [0] * n
        for i in range(n):
            idx = bisect(b, a[i])
            if idx >= m: idx = m - 1
            if idx > 0 and abs(a[i] - b[idx - 1]) <= abs(a[i] - b[idx]): idx -= 1
            c[i] = b[idx]
        print(sum(c))