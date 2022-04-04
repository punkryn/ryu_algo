# https://www.acmicpc.net/problem/15886
import sys
si = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    n = int(si())
    MAP = si().strip()
    visited = [0] * n
    ans = [i for i in range(n)]
    for i in range(n):
        if MAP[i] == 'E':
            for j in range(i + 1, n):
                if find_parent(ans, i) != find_parent(ans, j):
                    union(ans, i, j)
                if MAP[j] == 'W':
                    break
        elif MAP[i] == 'W':
            for j in range(i - 1, -1, -1):
                if find_parent(ans, i) != find_parent(ans, j):
                    union(ans, i, j)
                if MAP[j] == 'E':
                    break
    
    answer = set()
    for i in range(n):
        answer.add(find_parent(ans, i))

    print(len(answer))