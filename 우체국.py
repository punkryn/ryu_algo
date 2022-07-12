# https://www.acmicpc.net/problem/2141
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    xa = sorted([list(mis()) for _ in range(n)])
    total = sum([xa[i][1] for i in range(n)])
    cur = 0
    for i in range(n):
        cur += xa[i][1]
        if cur >= (total + 1) // 2:
            print(xa[i][0])
            break