# https://www.acmicpc.net/problem/1414
import sys
si = sys.stdin.readline

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
    graph = [si().strip() for _ in range(n)]
    parent = [i for i in range(n + 1)]
    alpha = dict()
    for i in range(ord('a'), ord('z') + 1):
        alpha[chr(i)] = i - ord('a') + 1
    for i in range(ord('A'), ord('Z') + 1):
        alpha[chr(i)] = i - ord('A') + 27
    
    edges = []
    total = 0
    v = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '0': continue
            total += alpha[graph[i][j]]
            if i == j:
                continue
            edges.append((alpha[graph[i][j]], i, j))
    edges.sort()
    for cost, x, y in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
            v += cost
    
    prev = find_parent(0)
    for i in range(1, n):
        cur = find_parent(i)
        if prev != cur:
            print(-1)
            exit()
        prev = cur

    if n == 1:
        if graph[0][0] == '0':
            print(0)
        else:
            print(alpha[graph[0][0]])
    else:
        print(total - v)