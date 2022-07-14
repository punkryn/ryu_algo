# https://www.acmicpc.net/problem/1976
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

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
    m = int(si())
    matrix = [list(mis()) for _ in range(n)]
    plan = list(mis())
    
    parent = [i for i in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j]:
                if find_parent(i + 1) != find_parent(j + 1):
                    union(i + 1, j + 1)
    
    prev = find_parent(plan[0])
    for i in range(1, m):
        cur = find_parent(plan[i])
        if prev != cur:
            print('NO')
            break
        prev = cur
    else:
        print('YES')