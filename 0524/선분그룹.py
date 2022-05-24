# https://www.acmicpc.net/problem/2162
from sys import stdin
from collections import defaultdict
si = stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    res = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if res > 0: return 1
    elif res < 0: return -1
    return 0

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    n = int(si())
    c = [list(map(int, si().split())) for _ in range(n)]
    
    parent = [i for i in range(n)]

    for i in range(n - 1):
        x1, y1, x2, y2 = c[i]
        for j in range(i + 1, n):
            a1, b1, a2, b2 = c[j]
            op = ccw(x1, y1, x2,y2, a1, b1) * ccw(x1, y1, x2, y2, a2, b2)
            op2 = ccw(a1, b1, a2, b2, x1, y1) * ccw(a1, b1, a2, b2, x2, y2)
            
            if op == 0 and op2 == 0:
                if min(x1, x2) <= max(a1, a2) and max(x1, x2) >= min(a1, a2) and min(y1, y2) <= max(b1, b2) and min(b1, b2) <= max(y1, y2):
                    union(i, j)
            elif op <= 0 and op2 <= 0:
                union(i, j)
            
    
    ans = defaultdict(int)
    for i in parent:
        ans[find_parent(i)] += 1
    
    print(len(ans))
    print(max(ans.values()))