import sys
si = sys.stdin.readline
n = int(si())
props = list(map(int, si().split()))
props.sort()

l, r, ans = 0, n-1, int(1e9) * 2
v1, v2 = 0, 0
while l < r:
    if abs(props[l] + props[r]) < ans:
        ans = abs(props[l] + props[r])
        v1, v2 = props[l], props[r]
    
    if props[l] + props[r] > 0:
        r -= 1
    else:
        l += 1
print(v1, v2)