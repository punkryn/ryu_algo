# https://www.acmicpc.net/problem/2636
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    cand = []
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue
            
            if board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
            else:
                cand.append((nx, ny))
                visited[nx][ny] = True
    return cand

if __name__ == '__main__':
    n, m = map(int, si().split())
    board = [list(map(int, si().split())) for _ in range(n)]
    
    ans = 0
    h = []
    while True:
        cand = bfs()
        if not cand:
            break
        
        ans += 1
        h.append(len(cand))
        for x, y in cand:
            board[x][y] = 0
    print(ans)
    print(h[-1])