# https://www.acmicpc.net/problem/21609
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
BLANK = -2

def DFS(x, y, visited, color):
    blocks = []
    normal = []
    stack = []
    stack.append((x, y))
    blocks.append((x, y))
    normal.append((x, y))
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny] != 0:
                continue
            if grid[nx][ny] == -1 or grid[nx][ny] == -2:
                continue

            if grid[nx][ny] != 0 and grid[nx][ny] != color:
                continue
            stack.append((nx, ny))
            blocks.append((nx, ny))
            if grid[nx][ny] > 0:
                normal.append((nx, ny))
            visited[nx][ny] = 1
    if normal:
        standard = min(normal, key=lambda x: (x[0], x[1]))
    else:
        standard = tuple()
    return blocks, standard, normal

def revisit(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0 and grid[i][j] == 0:
                visited[i][j] = 0

def find_biggest_block_group():
    visited = [[0] * n for _ in range(n)]
    block_groups = []
    for i in range(n):
        for j in range(n):
                # 일반블록 >= 1, 검은블록x, 무지개블록o, 그룹크기 >= 2
                # 기준블록 행, 열 기준 작은 것
            if grid[i][j] == 0 or grid[i][j] == -1 or grid[i][j] == -2:
                continue
            if visited[i][j] != 0: continue
            blocks, standard, normal = DFS(i, j, visited, grid[i][j])
            if len(blocks) >= 2 and len(normal) >= 1 and standard:
                block_groups.append([blocks, standard, normal])
            
            revisit(visited)
    
    if block_groups:
        group = max(block_groups, key=lambda x: (len(x[0]), len(x[0]) - len(x[2]), x[1][0], x[1][1]))
    else:
        group = tuple()
    return group

def remove_block(group):
    cnt = 0
    for block in group:
        cnt += 1
        x, y = block
        grid[x][y] = -2
    return cnt * cnt

def gravity():
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if grid[i][j] == -1 or grid[i][j] == -2:
                continue
            move(i, j)

def move(x, y):
    tmp = grid[x][y]
    grid[x][y] = -2
    while x + 1 < n and grid[x + 1][y] == -2:
        x += 1
    grid[x][y] = tmp

def rotate():
    stack = []
    for i in range(n):
        for j in range(n):
            stack.append((i, j, grid[i][j]))
    
    for i, j, v in stack:
        x, y = ((n - 1) * j + (n - 1)) % n, i
        grid[x][y] = v

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [list(map(int, si().split())) for _ in range(n)]

    score = 0
    while True:
        group = find_biggest_block_group()
        if not group:
            break
        score += remove_block(group[0])
        gravity()
        rotate()
        gravity()
        
    print(score)