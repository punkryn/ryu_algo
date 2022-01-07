# https://www.acmicpc.net/problem/1015

import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
tmp = []
for i in range(n):
    tmp.append([A[i], i])
tmp.sort()
# print(tmp)

P = [0] * n
for i, t in enumerate(tmp):
    a, b = t
    P[b] = str(i)
# print(P)
sys.stdout.write(' '.join(P))