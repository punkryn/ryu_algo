# https://www.acmicpc.net/problem/2805

def cal(mid, trees):
    total = 0
    for tree in trees:
        if tree > mid:
            total += (tree - mid)
    return total

import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
maximum = int(1e9)
start = 0
end = maximum
while start < end:
    mid = (start + end) // 2
    height = cal(mid, trees)
    # print(height)
    if m > height:
        end = mid
    else:
        start = mid + 1
print(end-1)