# https://www.acmicpc.net/problem/14391
import sys
si = sys.stdin.readline

def direction(x, y, length, d, f):
    if f == 0:
        if d == 0:
            ny = y
            for i in range(length + 1):
                if visited[x][ny]:
                    return False
                ny += 1
            for i in range(length + 1):
                visited[x][y] = 1
                y += 1
        else:
            nx = x
            for i in range(length + 1):
                if visited[nx][y]:
                    return False
                nx += 1
            for i in range(length + 1):
                visited[x][y] = 1
                x += 1
    elif f == 1:
        if d == 0:
            for i in range(length + 1):
                visited[x][y] = 0
                y += 1
        else:
            for i in range(length + 1):
                visited[x][y] = 0
                x += 1
    return True

def go(x, y, total):
    global ans
    if x == n:
        ans = max(ans, total)
        return

    nx = x
    ny = y + 1
    if ny == m:
        nx = x + 1
        ny = 0
    if visited[x][y]:
        go(nx, ny, total)
        return


    for i in range(m - y):
        if not direction(x, y, i, 0, 0):
            continue
        go(nx, ny, total + int(paper[x][y: y + i + 1]))
        direction(x, y, i, 0, 1)
    
    for i in range(n - x):
        if not direction(x, y, i, 1, 0):
            continue
        tmp = ''
        for j in range(i + 1):
            tmp += paper[x + j][y]
        go(nx, ny, total + int(tmp))
        direction(x, y, i, 1, 1)

if __name__ == '__main__':
    n, m = map(int, si().split())
    paper = [si().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    ans = 0
    go(0, 0, 0)
    print(ans)
