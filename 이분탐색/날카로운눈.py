# https://www.acmicpc.net/problem/1637
import sys
si = sys.stdin.readline
n = int(si())
seq = [list(map(int, si().split())) for _ in range(n)]

def count(A, C, B, X):
    if X < A: return 0
    if C < X: return (C - A) // B + 1
    return (X - A) // B + 1

def deter(cand):
    total = 0
    for i in seq:
        total += count(i[0], i[1], i[2], cand)
    return total % 2 == 1

l, r, ans, ansCnt = 1, 1 << 31, 0, 0
while l <= r:
    mid = (l + r) // 2
    if deter(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

if ans == 0:
    print('NOTHING')
else:
    for i in seq:
        if i[0] <= ans <= i[1] and (ans - i[0]) % i[2] == 0:
            ansCnt += 1
    print(ans, ansCnt)