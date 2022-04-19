# https://www.acmicpc.net/problem/16954
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dy = [0, 1, 1, 1, 0, -1, -1, -1, 0]

def wall_move():
    board.pop()
    board.appendleft('........')

def bfs():
    q = deque()
    q.append((w_pos, 0))

    visited = [[0] * 8 for _ in range(8)]
    cur_time = 0
    while q:
        pos, time = q.popleft()
        x, y = pos

        if [x, y] == goal:
            return 1

        if cur_time < time:
            cur_time += 1
            wall_move()
            visited = [[0] * 8 for _ in range(8)]
        
        if board[x][y] == '#':
            continue
        
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < 8 and 0 <= ny < 8) or board[nx][ny] == '#' or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append(((nx, ny), time + 1))
    return 0

if __name__ == '__main__':
    board = deque()
    for _ in range(8):
        board.append(si().strip())
    w_pos = [7, 0]
    goal = [0, 7]
    print(bfs())