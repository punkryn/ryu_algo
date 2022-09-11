# https://www.acmicpc.net/problem/16956
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    r, c = mis()
    MAP = [list(si().strip()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == 'S':
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if not (0 <= ni < r and 0 <= nj < c): continue
                    if MAP[ni][nj] != '.': continue
                    MAP[ni][nj] = 'D'
    
    visited = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if visited[i][j] or MAP[i][j] != 'W': continue
            st = [(i, j)]
            visited[i][j] = True
            while st:
                x, y = st.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not (0 <= nx < r and 0 <= ny < c): continue
                    if visited[nx][ny]: continue
                    if MAP[nx][ny] == 'D' or MAP[nx][ny] == 'W': continue
                    visited[nx][ny] = True
                    st.append((nx, ny))
                    if MAP[nx][ny] == 'S':
                        print(0)
                        exit()
    print(1)
    print('\n'.join([''.join(row) for row in MAP]))