# https://www.acmicpc.net/problem/10775
from sys import stdin
si = stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    
    parent[y] = x

if __name__ == "__main__":
    g = int(si())
    p = int(si())
    
    parent = [i for i in range(g + 1)]
    ans = 0
    for _ in range(p):
        g_ = int(si())
        fg = find_parent(g_)
        if fg == 0:
            print(ans)
            exit()
        ans += 1
        union(fg - 1, fg)
    print(ans)