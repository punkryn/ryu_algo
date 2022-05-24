# https://www.acmicpc.net/problem/10942
from sys import stdin
si = stdin.readline
if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))

    f = [[False] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(i + k, i + k + 1):
                if j >= n: break
                if i == j:
                    f[i][j] = True
                elif i + 1 == j and a[i] == a[j]:
                    f[i][j] = True
                elif a[i] == a[j] and f[i + 1][j - 1]:
                    f[i][j] = True

    for _ in range(int(si())):
        s, e = map(int, si().split())
        print(1 if f[s - 1][e - 1] else 0)