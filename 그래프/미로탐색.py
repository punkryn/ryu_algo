# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(maze, n, m):
    q = deque()
    q.append((0, 0, 1))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        cur = q.popleft()
        x, y, cnt = cur
        for i in range(4):
            nx = x + dx[i]        
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] != 0: continue
                if maze[nx][ny] == '0': continue
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = cnt + 1
    return visited[n-1][m-1]    

def main():
    n, m = map(int, si().split())
    maze = [si().strip() for _ in range(n)]
    print(bfs(maze, n, m))

if __name__ == '__main__':
    main()