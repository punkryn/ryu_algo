# https://www.acmicpc.net/problem/11441
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = list(mis())
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i - 1]
    m = int(si())
    for _ in range(m):
        i, j = mis()
        print(ps[j] - ps[i - 1])