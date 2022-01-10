# https://www.acmicpc.net/problem/3273
import sys
n = int(sys.stdin.readline())
seq = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

def bs(arr, l, r, target):
    while l <= r:
        mid = (l + r)//2
        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return 0

cnt = 0
for i in range(n):
    cnt += bs(seq, i + 1, n - 1, x - seq[i])
print(cnt)