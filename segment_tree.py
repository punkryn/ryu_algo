# 12
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# 2 6
# 3 7
# 3 8
# 4 9
# 4 10
# 5 11
import sys
si = sys.stdin.readline

v = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
tree = [[] for _ in range(12)]

n = int(si())
for _ in range(n - 1):
    a, b = map(int, si().split())
    tree[a].append(b)
    tree[b].append(a)

ps = [0] * (n * 4)
def dfs(s, e, x):
    if s == e:
        ps[x] = v[s]
        return v[s]

    ret = 0
    mid = (s + e) // 2
    ret += dfs(s, mid, x * 2) + dfs(mid + 1, e, x * 2 + 1)

    ps[x] = ret
    return ret

def SUM(s, e, x, left, right):
    if left > e or right < s:
        return 0
    
    if left <= s and e <= right:
        return ps[x]
    
    mid = (s + e) // 2
    ret = 0
    ret += SUM(s, mid, x * 2, left, right) + SUM(mid + 1, e, x * 2 + 1, left, right)
    return ret

def UPDATE(s, e, x, v, value):
    if v < s or e < v:
        return
    
    ps[x] += value
    if s == e: return
    
    mid = (s + e) // 2
    UPDATE(s, mid, x * 2, v, value)
    UPDATE(mid + 1, e, x * 2 + 1, v, value)

dfs(0, n - 1, 1)
print(SUM(0, n - 1, 1, 4, 8))
print(ps)

UPDATE(0, n - 1, 1, 7, 2)
print(ps)