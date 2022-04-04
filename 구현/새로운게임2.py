# https://www.acmicpc.net/problem/17837
import sys
from collections import deque
si = sys.stdin.readline

WHITE, RED, BLUE = 0, 1, 2
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

if __name__ == '__main__':
    n, k = map(int, si().split())
    board = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, si().split())) for _ in range(n)]
    pos = dict()
    b = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, k + 1):
        x, y, d = map(int, si().split())
        pos[i] = [x, y, d]
        b[x][y].append(i)

    ans = 0
    while True:
        ans += 1
        if ans > 1000:
            print(-1)
            exit()
        for i in range(1, k + 1):
            x, y, d = pos[i]
            
            nx = x + dx[d]
            ny = y + dy[d]

            if (1 <= nx <= n and 1 <= ny <= n):
                if board[nx][ny] == WHITE:
                    q = []
                    for j, key in enumerate(b[x][y]):
                        if key == i:
                            q.extend(b[x][y][j:])
                            b[x][y] = b[x][y][:j]
                            break
                    
                    for num in q:
                        b[nx][ny].append(num)
                        pos[num][0], pos[num][1] = nx, ny

                    if len(b[nx][ny]) >= 4:
                        print(ans)
                        exit()
                        
                elif board[nx][ny] == RED:
                    q = []
                    for j, key in enumerate(b[x][y]):
                        if key == i:
                            q.extend(b[x][y][j:])
                            b[x][y] = b[x][y][:j]
                            break
                    
                    q = q[::-1]
                    
                    for num in q:
                        b[nx][ny].append(num)
                        pos[num][0], pos[num][1] = nx, ny

                    if len(b[nx][ny]) >= 4:
                        print(ans)
                        exit()

                elif board[nx][ny] == BLUE:
                    if d == 1 or d == 3: d += 1
                    elif d == 2 or d == 4: d -= 1
                    

                    nx = x + dx[d]
                    ny = y + dy[d]
                    if (1 <= nx <= n and 1 <= ny <= n):
                        if board[nx][ny] == BLUE:
                            continue
                    else:
                        continue
                    pos[i][2] = d

                    q = []
                    for j, key in enumerate(b[x][y]):
                        if key == i:
                            q.extend(b[x][y][j:])
                            b[x][y] = b[x][y][:j]
                            break
                    
                    for num in q:
                        b[nx][ny].append(num)
                        pos[num][0], pos[num][1] = nx, ny

                    if len(b[nx][ny]) >= 4:
                        print(ans)
                        exit()
            else:
                if d == 1 or d == 3: d += 1
                elif d == 2 or d == 4: d -= 1
                

                nx = x + dx[d]
                ny = y + dy[d]
                if (1 <= nx <= n and 1 <= ny <= n):
                    if board[nx][ny] == BLUE:
                        continue
                else:
                    continue
                pos[i][2] = d

                q = []
                for j, key in enumerate(b[x][y]):
                    if key == i:
                        q.extend(b[x][y][j:])
                        b[x][y] = b[x][y][:j]
                        break
                
                for num in q:
                    b[nx][ny].append(num)
                    pos[num][0], pos[num][1] = nx, ny

                if len(b[nx][ny]) >= 4:
                    print(ans)
                    exit()
        