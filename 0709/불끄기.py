# https://www.acmicpc.net/problem/14939
from re import L
from sys import stdin
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def click(x, y, tmp):
    tmp[x][y] = not tmp[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 10 and 0 <= ny < 10): continue
        tmp[nx][ny] = not tmp[nx][ny]

def isLight(tmp):
    for i in range(10):
        for j in range(10):
            if tmp[i][j]:
                return True
    return False

if __name__ == '__main__':
    a = [si().strip() for _ in range(10)]
    state = [[False] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'O':
                state[i][j] = True
    ans = int(1e9)
    for i in range((1 << 10)):
        cnt = 0
        tmp = [row[:] for row in state]
        
        for j in range(10):
            if i & (1 << j):
                cnt += 1
                click(0, j, tmp)
        
        for x in range(1, 10):
            for y in range(10):
                if tmp[x - 1][y]:
                    click(x, y, tmp)
                    cnt += 1
        if not isLight(tmp):
            ans = min(ans, cnt)
    
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)