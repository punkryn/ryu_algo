# https://www.acmicpc.net/problem/17837
import sys
from collections import deque
si = sys.sdtin.readline

WHITE, RED, BLUE = 0, 1, 2
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

if __name__ == '__main__':
    n, k = map(int, si().split())
    board = [list(map(int, si().split())) for _ in range(n)]
    pos = dict()
    b = [[deque() for _ in range(n)] for _ in range(n)]
    for i in range(k):
        x, y, d = map(int, si().split())
        pos[i] = [x, y, d]
        b[x][y].append(i)

    while True:
        for i in range(1, k + 1):
            x, y, d = pos[i]
            
            nx = x + dx[d]
            ny = y + dy[d]

            if (0 <= nx < n and 0 <= ny < n):
                if board[nx][ny] == WHITE:
                    q = deque()
                    while b[x][y] and b[x][y][-1] != i:
                        q.append(b[x][y].pop())
                    # if b[nx][ny][-1] == i:
                    q.append(b[x][y].pop())
                    while q:
                        cur = q.pop()
                        pos[cur][0], pos[cur][1] = nx, ny
                        b[nx][ny].append(cur)
                        
                elif board[nx][ny] == RED:
                    q = deque()
                    while b[x][y] and b[x][y][-1] != i:
                        q.append(b[x][y].pop())
                    q.append(b[x][y].pop())
                    while q:
                        cur = q.popleft()
                        pos[cur][0], pos[cur][1] = nx, ny
                        b[nx][ny].append(cur)

                elif board[nx][ny] == BLUE:
                    q = deque()
                    

                    while b[x][y] and b[x][y][-1] != i:
                        q.append(b[x][y].pop())
                    q.append(b[x][y].pop())
                    while q:
                        cur = q.pop()
                        

            else:
