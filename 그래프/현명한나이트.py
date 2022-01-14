# https://www.acmicpc.net/problem/18404
import sys
from collections import deque
si = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def main():
    n, m = map(int, si().split())
    x, y = map(int, si().split())
    pos = [list(map(int, si().split())) for _ in range(m)]
    visited = [[-1] * (n + 1) for _ in range(n+1)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        cur = q.popleft()
        for i in range(8):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                if visited[nx][ny] != -1: continue
                visited[nx][ny] = visited[cur[0]][cur[1]] + 1
                q.append((nx, ny))
    
    for p in pos:
        print(visited[p[0]][p[1]], end=' ')

if __name__ == '__main__':
    main()