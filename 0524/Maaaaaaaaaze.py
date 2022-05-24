# https://www.acmicpc.net/problem/16985
import sys
from itertools import permutations
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def rotate(board):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][5 - i - 1] = board[i][j]
    return tmp

def go(depth, cur, per):
    global ans
    if depth == 5:
        cube = make_cube(cur, per)
        abc=123
        # for x, y, z in [[0, 0, 0], [0, 4, 0], [4, 0, 0], [4, 4, 0]]:
        for x, y, z in [[0, 0, 0]]:
            if cube[x][y][z] == 0: continue
            dist = bfs(cube, (x, y, z), (4 - x, 4 - y, 4 - z))
            if dist == -1:
                ans = max(ans, dist)
            else:
                ans = min(ans, dist)
        return
    
    for i in range(4):
        cur.append(i)
        go(depth + 1, cur, per)
        cur.pop()

def make_cube(cur, per):
    cube = []
    for i in range(5):
        cube.append(rotated[per[i]][cur[i]])
    return cube

def bfs(cube, start, end):
    if cube[end[0]][end[1]][end[2]] == 0:
        return -1
    q = deque()
    q.append(start)
    visited = [[[-1] * 5 for _ in range(5)] for __ in range(5)]
    visited[start[0]][start[1]][start[2]] = 0
    while q:
        x, y, z = q.popleft()
        
        if x == end[0] and y == end[1] and z == end[2]:
            break

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if not (0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5) or visited[nx][ny][nz] != -1 or cube[nx][ny][nz] == 0:
                continue
            
            visited[nx][ny][nz] = visited[x][y][z] + 1
            q.append((nx, ny, nz))
    return visited[end[0]][end[1]][end[2]]

if __name__ == '__main__':
    boards = [[list(map(int, si().split())) for _ in range(5)] for __ in range(5)]
    
    rotated = []
    for i in range(5):
        tmp = []
        tmp.append(boards[i])
        r1 = rotate(boards[i])
        tmp.append(r1)
        r2 = rotate(r1)
        tmp.append(r2)
        r3 = rotate(r2)
        tmp.append(r3)
        rotated.append(tmp)

    # for r in rotated:
    #     for v in r:
    #         for v1 in v:
    #             print(v1)
    #         print()
    ans = int(1e9)
    # 판 순서
    for per in permutations(list(range(5)), 5):
        # 회전 결정
        go(0, [], per)
    
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)