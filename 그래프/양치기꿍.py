# https://www.acmicpc.net/problem/3187
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    stack = []
    stack.append((x, y))
    visited[x][y] = 1

    sheep = 0
    wolf = 0
    while stack:
        x, y = stack.pop()
        if grid[x][y] == 'v':
            wolf += 1
        elif grid[x][y] == 'k':
            sheep += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < r and 0 <= ny < c) or visited[nx][ny] or grid[nx][ny] == '#':
                continue
            visited[nx][ny] = 1
            stack.append((nx, ny))
    return wolf, sheep


if __name__ == '__main__':
    r, c = map(int, si().split())
    grid = [si().strip() for _ in range(r)]

    t_wolf, t_sheep = 0, 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'v':
                t_wolf += 1
            elif grid[i][j] == 'k':
                t_sheep += 1
    
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if visited[i][j] or grid[i][j] =='#': continue
            wolf, sheep = DFS(i, j)
            if wolf >= sheep:
                t_sheep -= sheep
            else:
                t_wolf -= wolf
    print(t_sheep, t_wolf)