# https://www.acmicpc.net/problem/1944
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

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

def BFS(xs, ys, number, flag):
    q = deque()
    q.append((xs, ys))
    visited = [[-1] * n for _ in range(n)]
    visited[xs][ys] = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] != -1 or maze[nx][ny] == '1': continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

            if flag:
                checked[v[nx][ny]] = 1

            if maze[nx][ny] == 'S' or maze[nx][ny] == 'K':
                edges.append((number, v[nx][ny], visited[nx][ny]))

if __name__ == '__main__':
    n, m = map(int, si().split())
    maze = [si().strip() for _ in range(n)]
    edges = []
    v = [[0] * n for _ in range(n)]

    start_pos = []
    key_pos = []
    cnt = 0
    start_point = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if maze[i][j] == 'S':
                cnt += 1
                v[i][j] = cnt
                start_pos.append((i, j))
                start_point = cnt
            elif maze[i][j] == 'K':
                cnt += 1
                v[i][j] = cnt
                key_pos.append((i, j))
    
    checked = [0] * (cnt + 1)
    checked[start_point] = 1
    for x, y in start_pos:
        BFS(x, y, v[x][y], True)
    
    for i in range(1, cnt + 1):
        if checked[i] == 0:
            print(-1)
            exit()

    for x, y in key_pos:
        BFS(x, y, v[x][y], False)
    
    parent = [i for i in range(cnt + 1)]
    edges.sort(key=lambda x: x[2])
    ans = 0
    for x, y, z in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
            ans += z
    
    print(ans)