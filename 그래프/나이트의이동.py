# https://www.acmicpc.net/problem/7562
import sys
from collections import deque
si = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def main():
    t = int(si())
    for _ in range(t):
        l = int(si())
        sx, sy = map(int, si().split())
        ex, ey = map(int, si().split())
        
        def bfs():
            q = deque()
            q.append((sx, sy))
            visited = [[0] * l for _ in range(l)]
            visited[sx][sy] = 1
            while q:
                x, y = q.popleft()
                if x == ex and y == ey:
                    break
                
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < l and 0 <= ny < l:
                        if visited[nx][ny] != 0: continue
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1  
            return visited[ex][ey] - 1

        if sx == ex and sy == ey:
            print(0)
        else:
            print(bfs())

if __name__ == '__main__':
    main()