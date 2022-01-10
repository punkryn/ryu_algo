# https://www.acmicpc.net/problem/7795

def lower_bound(arr, left, right, target):
    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    B.sort()
    ans = 0
    for num in A:
        tmp = lower_bound(B, 0, len(B)-1, num)
        if B[tmp] < num:
            ans += tmp + 1
        else:
            ans += tmp
    print(ans)