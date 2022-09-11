# https://www.acmicpc.net/problem/4358
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    a = dict()
    total = 0
    for s in sys.stdin:
        if s == '\n': break
        s = s.strip()
        if s not in a:
            a[s] = 0
        a[s] += 1
        total += 1
    
    for key in sorted(a):
        print(f'{key} {(a[key] / total * 100):.4f}')