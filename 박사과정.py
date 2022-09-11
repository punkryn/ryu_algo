# https://www.acmicpc.net/problem/5026
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    for _ in range(n):
        p = si().strip()
        if p == 'P=NP':
            print('skipped')
        else:
            a, b = p.split('+')
            print(int(a) + int(b))