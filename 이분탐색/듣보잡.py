# https://www.acmicpc.net/problem/1764
import sys
n, m = map(int, sys.stdin.readline().split())
D = list(sys.stdin.readline().strip() for _ in range(n))
B = list(sys.stdin.readline().strip() for _ in range(m))
D.sort()
B.sort()
def bs(l, r, target):
    while l <= r:
        mid= (l + r)//2
        if B[mid] == target:
            return 1
        if B[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return 0

cnt = 0
ans = []
for d in D:
    tmp = bs(0, m - 1, d)
    if tmp:
        cnt += 1
        ans.append(d)

sys.stdout.write(str(cnt) + '\n')
for a in ans:
    sys.stdout.write(a + '\n')