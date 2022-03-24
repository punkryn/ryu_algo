# https://www.acmicpc.net/problem/4179
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    r, c = map(int, si().split())
    maze = [si().strip() for _ in range(r)]
    
    trace = [[-1] * c for _ in range(r)]

    pos = [0, 0]
    fires = []
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'J':
                pos[0] = i
                pos[1] = j
            if maze[i][j] == 'F':
                fires.append([i, j])

    q_ = deque()
    for fire in fires:
        q_.append((fire, 0))
        trace[fire[0]][fire[1]] = 0
    while q_:
        cur_, t_ = q_.popleft()
        for i in range(4):
            x_, y_ = cur_
            fx = x_ + dx[i]
            fy = y_ + dy[i]
            if not (0 <= fx < r and 0 <= fy < c):
                continue
            if maze[fx][fy] == '#':
                continue
            if trace[fx][fy] != -1:
                continue
            trace[fx][fy] = t_ + 1
            q_.append(((fx, fy), t_ + 1))

    q = deque()
    q.append((pos, 0))
    visited = [[0] * c for _ in range(r)]
    visited[pos[0]][pos[1]] = 1

    ans = 'IMPOSSIBLE'
    while q:
        cur, t = q.popleft()
        
        if cur[0] == 0 or cur[0] == r - 1 or cur[1] == 0 or cur[1] == c - 1:
            ans = t + 1
            break

        for i in range(4):
            x, y = cur
            nx = x + dx[i]
            ny = y + dy[i]


            if visited[nx][ny] != 0:
                continue
            
            if trace[nx][ny] != -1 and trace[nx][ny] <= t + 1:
                continue

            if maze[nx][ny] != '.':
                continue

            

            visited[nx][ny] = 1
            q.append(((nx, ny), t + 1))
    
    print(ans)