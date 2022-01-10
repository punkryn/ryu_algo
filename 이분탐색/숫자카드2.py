# https://www.acmicpc.net/problem/10816
from sys import stdin
from sys import stdout
import bisect
n = int(stdin.readline())
cards = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
find = list(map(int, stdin.readline().split()))

def lower_bound(arr, l, r, target):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    # print('l', r)
    return res

def upper_bound(arr, l, r, target):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    # print('r', r)
    return res
    
for num in find:
    ub = upper_bound(cards, 0, n - 1, num)
    lb = lower_bound(cards, 0, n - 1, num)
    # ub = bisect.bisect_right(cards, num)
    # lb = bisect.bisect_left(cards, num)
    tmp = ub - lb
    stdout.write(str(tmp) + ' ')