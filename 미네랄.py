# https://www.acmicpc.net/problem/2933
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def throw(height, flag):
    if flag:
        for i in range(c):
            if grid[-height][i] == 'x':
                grid[-height][i] = '.'
                return True
        return False
    else:
        for i in range(c - 1, -1, -1):
            if grid[-height][i] == 'x':
                grid[-height][i] = '.'
                return True
        return False

def cluster_check():
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if visited[i][j] or grid[i][j] == '.': continue
            stack = []
            stack.append((i, j))
            visited[i][j] = 1
            max_x = -1
            cluster = []
            cluster.append((i, j))
            while stack:
                x, y = stack.pop()
                max_x = max(max_x, x)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < r and 0 <= ny < c) or visited[nx][ny] or grid[nx][ny] == '.':
                        continue
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
                    cluster.append((nx, ny))
            
            if max_x < r - 1:
                fall(cluster)
                return

def fall(cluster):
    floor = dict()
    for x, y in cluster:
        if y not in floor:
            floor[y] = x
        else:
            floor[y] = max(floor[y], x)

    fall_height = r + 1
    for key in floor:
        for i in range(floor[key] + 1, r):
            if grid[i][key] == 'x':
                fall_height = min(fall_height, i - floor[key] - 1)
                break
        else:
            fall_height = min(fall_height, r - 1 - floor[key])
    
    for x, y in cluster:
        grid[x][y] = '.'
    
    if fall_height > 0:
        for x, y in cluster:
            grid[x + fall_height][y] = 'x'

if __name__ == '__main__':
    r, c = map(int, si().split())
    grid = [list(si().strip()) for _ in range(r)]
    n = int(si())
    queries = list(map(int, si().split()))
    for i in range(n):
        # l -> r
        height = queries[i]
        if i % 2 == 0:
            # 맞아야 클러스터 체크
            if throw(height, 1):
                cluster_check()
        else:
            if throw(height, 0):
                cluster_check()
    for g in grid:
        print(''.join(g))