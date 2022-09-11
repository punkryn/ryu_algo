# https://www.acmicpc.net/problem/2428
import sys
from bisect import bisect_left, bisect_right
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = sorted(list(map(lambda x: x * 100, mis())))

    ans = 0
    for i in range(n - 1, 0, -1):
        l, r = bisect_left(a, a[i] * 0.9, 0, i - 1), bisect_right(a, a[i], 0, i - 1)

        if l == r and (a[i] * 0.9 > a[l] or a[i] < a[l]):
            continue

        ans += r - l + 1
    print(ans)