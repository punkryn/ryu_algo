# https://www.acmicpc.net/problem/11399
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = sorted(list(map(int, si().split())))
    ps = [0] * n
    ps[0] = a[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + a[i]
    print(sum(ps))