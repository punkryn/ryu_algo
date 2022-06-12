# https://www.acmicpc.net/problem/2151
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)

if __name__ == '__main__':
    n = int(si())
    home = [si().strip() for _ in range(n)]
    door_pos = [(i, j) for i in range(n) for j in range(n) if home[i][j] == '#']
    
    q = deque()
    visited = [[[INF] * 4 for _ in range(n)] for __ in range(n)]
    for i in range(4):
        q.append([*door_pos[0], i])
        visited[door_pos[0][0]][door_pos[0][1]][i] = 0

    while q:
        x, y, d = q.popleft()

        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n): continue
        if home[nx][ny] == '*': continue
        if home[nx][ny] == '.' or home[nx][ny] == '#':
            if visited[nx][ny][d] <= visited[x][y][d]: continue
            visited[nx][ny][d] = visited[x][y][d]
            q.append([nx, ny, d])
        else:
            if d == 0 or d == 2:
                nxt_d = [1, 3]
            else:
                nxt_d = [0, 2]
            
            for nd in nxt_d:
                if visited[nx][ny][nd] > visited[x][y][d]:
                    visited[nx][ny][nd] = visited[x][y][d] + 1
                    q.append([nx, ny, nd])
            
            if visited[nx][ny][d] > visited[x][y][d]: 
                visited[nx][ny][d] = visited[x][y][d]
                q.append([nx, ny, d])
    
    ans = INF
    for c in visited[door_pos[1][0]][door_pos[1][1]]:
        ans = min(ans, c)
    print(ans)
# 5
# *****
# *!.!*
# #.!!#
# *.!!*
# *****