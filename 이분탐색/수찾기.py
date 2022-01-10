# https://www.acmicpc.net/problem/1920
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
A.sort()

def bs(l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if A[mid] < target:
            l = mid + 1
        elif A[mid] > target:
            r = mid - 1
        else:
            return 1
    return 0

for a in arr:
    sys.stdout.write(str(bs(0, n - 1, a)) + '\n')