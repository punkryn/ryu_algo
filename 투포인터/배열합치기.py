# https://www.acmicpc.net/problem/11728
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
A = list(map(int, si().split()))
B = list(map(int, si().split()))
ap, bp = 0, 0

while ap < n and bp < m:
    if A[ap] < B[bp]:
        print(A[ap], end=' ')
        ap += 1
    elif A[ap] > B[bp]:
        print(B[bp], end=' ')
        bp += 1
    else:
        print(A[ap], end=' ')
        print(B[bp], end=' ')
        ap += 1
        bp += 1

while ap < n:
    print(A[ap], end=' ')
    ap += 1

while bp < m:
    print(B[bp], end=' ')
    bp += 1
