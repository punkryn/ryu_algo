# https://www.acmicpc.net/problem/13144
import sys
si = sys.stdin.readline
n = int(si())
seq = list(map(int, si().split()))

r = -1
ans = 0
# cand = set()
# for l in range(n):
#     while r + 1 < n and seq[r + 1] not in cand:
#         r += 1
#         cand.add(seq[r])
#     # print(r, l)
#     ans += r - l + 1
#     cand.remove(seq[l])

visited = [0] * 100001
for l in range(n):
    while r + 1 < n and visited[seq[r + 1]] == 0:
        r += 1
        visited[seq[r]] = 1
    ans += r - l + 1
    visited[seq[l]] = 0
    
print(ans)