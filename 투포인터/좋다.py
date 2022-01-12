# https://www.acmicpc.net/problem/1253
import sys
si = sys.stdin.readline
n = int(si())
A = list(map(int, si().split()))
A.sort()

ans = 0
for i in range(n):
    l, r = 0, n - 1
    while l < r:
        if l == i: l += 1
        elif r == i: r-= 1
        else:
            if A[l] + A[r] > A[i]:
                r -= 1
            elif A[l] + A[r] < A[i]:
                l += 1
            else:
                ans += 1
                break
print(ans)