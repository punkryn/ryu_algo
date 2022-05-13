# https://www.acmicpc.net/problem/20665
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    n, t, p = map(int, si().split())
    timestamp = [0] * (60 * 21 + 1)
    order = []
    for _ in range(t):
        start, end = si().split()
        start = int(start[:2]) * 60 + int(start[2:])
        end = int(end[:2]) * 60 + int(end[:2])
        order.append((start, end, end - start))
    order.sort(key=lambda x: (x[0], x[2]))
    