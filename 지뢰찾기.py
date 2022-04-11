# https://www.acmicpc.net/problem/4396
import sys
si = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

if __name__ == '__main__':
    n = int(si())
    grid = [si().strip() for _ in range(n)]
    played = [si().strip() for _ in range(n)]

    board = [['.' for _ in range(n)] for __ in range(n)]
    flag = False
    pos = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                pos.append((i, j))
            
            if played[i][j] == '.':
                continue
                
            if grid[i][j] == '*':
                flag = True

            cnt = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (0 <= ni < n and 0 <= nj < n): continue
                if grid[ni][nj] == '*':
                    cnt += 1
            board[i][j] = str(cnt)
    
    if flag:
        for x, y in pos:
            board[x][y] = '*'

    for i in range(n):
        print(''.join(board[i]))