# https://www.acmicpc.net/problem/1987
from sys import stdin
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y, depth):
    global ans
    ans = max(ans, depth)
    if ans == 26:
        print(ans)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < r and 0 <= ny < c) or visited[nx][ny]:
            continue
        idx = ord(board[nx][ny]) - ord('A')
        if alpha[idx]:
            continue

        visited[nx][ny] = True
        alpha[idx] = True
        go(nx, ny, depth + 1)
        alpha[idx] = False
        visited[nx][ny] = False

if __name__ == '__main__':
    r, c = map(int, si().split())
    board = [si().strip() for _ in range(r)]
    alpha = [False] * 26
    visited = [[False] * c for _ in range(r)]
    ans = 0
    visited[0][0] = True
    alpha[ord(board[0][0]) - ord('A')] = True
    go(0, 0, 1)
    print(ans)