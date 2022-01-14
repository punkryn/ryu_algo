# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
si = sys.stdin.readline

def main():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    r, c = map(int, si().split())
    MAP = [list(si().strip()) for _ in range(r)]
    water = []
    rock = []
    start, end = (), ()
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == 'S':
                start = (i, j)
            elif MAP[i][j] == 'D':
                end = (i, j)
            elif MAP[i][j] == '*':
                water.append((i, j))
            elif MAP[i][j] == 'X':
                rock.append((i, j))

    q = deque()
    q.append((start, 0))
    visited = [[0] * c for _ in range(r)]
    visited[start[0]][start[1]] = 1

    prev = -1
    while q:
        cur, cnt = q.popleft()
        x, y = cur

        tmp = []
        if cnt > prev:
            prev = cnt
            for i in range(r):
                for j in range(c):
                    if MAP[i][j] == '*':
                        for k in range(4):
                            ix = i + dx[k]
                            jy = j + dy[k]
                            if 0 <= ix < r and 0 <= jy < c and MAP[ix][jy] == '.':
                                tmp.append((ix, jy))

            for t in tmp:
                MAP[t[0]][t[1]] = '*'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] != 0: continue
                if MAP[nx][ny] == '*' or MAP[nx][ny] == 'X': continue
                visited[nx][ny] = visited[x][y] + 1
                q.append(((nx, ny), cnt + 1))

    if visited[end[0]][end[1]] == 0:
        print('KAKTUS')
    else:
        print(visited[end[0]][end[1]] - 1)

if __name__ == '__main__':
    main()
