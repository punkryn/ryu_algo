# https://www.acmicpc.net/problem/15683
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# ºÏ µ¿ ³² ¼­
def mark(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    marking[x][y] = 1
    while 0 <= nx < n and 0 <= ny < m:
        if MAP[nx][ny] == 6:
            break
        marking[nx][ny] += 1
        nx += dx[d]
        ny += dy[d]

def recover(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    marking[x][y] = 0
    while 0 <= nx < n and 0<= ny < m:
        if MAP[nx][ny] == 6:
            break
        marking[nx][ny] -= 1
        nx += dx[d]
        ny += dy[d]

def count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if marking[i][j] == 0:
                cnt += 1
    return cnt

def go(depth):
    global ans
    if depth == cctv_cnt:
        ans = min(count(), ans)
        return
    
    x, y, c = cctv[depth]
    if c == 1:
        for i in range(4):
            mark(x, y, i)
            go(depth + 1)
            recover(x, y, i)
    elif c == 2:
        for i in range(2):
            mark(x, y, i)
            mark(x, y, i + 2)
            go(depth + 1)
            recover(x, y, i + 2)
            recover(x, y, i)
    elif c == 3:
        for i in range(4):
            mark(x, y, i)
            mark(x, y, (i + 1) % 4)
            go(depth + 1)
            recover(x, y, (i + 1) % 4)
            recover(x, y, i)
    elif c == 4:
        for i in range(4):
            mark(x, y, i)
            mark(x, y, (i + 1) % 4)
            mark(x, y, (i + 3) % 4)
            go(depth + 1)
            recover(x, y, (i + 3) % 4)
            recover(x, y, (i + 1) % 4)
            recover(x, y, i)
    else:
        for i in range(4):
            mark(x, y, i)
        go(depth + 1)
        for i in range(4):
            recover(x, y, i)

if __name__ == '__main__':
    n, m = map(int, si().split())
    MAP = [list(map(int, si().split())) for _ in range(n)]
    cctv = []
    marking = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if MAP[i][j] != 0 and MAP[i][j] != 6:
                cctv.append((i, j, MAP[i][j]))
            
            if MAP[i][j] == 6:
                marking[i][j] = 2
    
    cctv_cnt = len(cctv)
    ans = n * m
    go(0)
    print(ans)