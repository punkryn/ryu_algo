# https://www.acmicpc.net/problem/2470

def lower_bound(arr, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

import sys
n = int(sys.stdin.readline())
props = list(map(int, sys.stdin.readline().split()))
props.sort()

best_sum = 10e10
v1, v2 = 0, 0
for i in range(n-1):
    cand = lower_bound(props, i + 1, n - 1, -props[i])
    
    if i < cand - 1 and abs(props[i] + props[cand-1]) < best_sum:
        best_sum = abs(props[i] + props[cand-1])
        v1, v2 = props[i], props[cand-1]
    
    if abs(props[i] + props[cand]) < best_sum:
        best_sum = abs(props[i] + props[cand])
        v1, v2 = props[i], props[cand]

print(v1, v2)