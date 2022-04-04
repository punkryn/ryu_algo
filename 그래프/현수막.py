# https://www.acmicpc.net/problem/14716
import sys
si = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def DFS(x, y, visited):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or card[nx][ny] == 0 or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = 1
            stack.append((nx, ny))

if __name__ == '__main__':
    n, m = map(int, si().split())
    card = [list(map(int, si().split())) for _ in range(n)]
    
    visited = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 or card[i][j] == 0:
                continue
            ans += 1
            DFS(i, j, visited)
    print(ans)