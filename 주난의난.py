# https://www.acmicpc.net/problem/14497
import sys
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = map(int, si().split())
    x1, y1, x2, y2 = map(int, si().split())
    MAP = ['1' * (m + 1)] + ['1' + si().strip() for _ in range(n)]
    
    q0 = deque([(x1, y1)])
    q1 = deque()
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[x1][y1] = True
    cnt = 0
    while q0 or q1:
        x, y = q0.popleft()
        if x == x2 and y == y2:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (1 <= nx <= n and 1 <= ny <= m) or visited[nx][ny]:
                continue
            
            if MAP[nx][ny] == '0':
                visited[nx][ny] = True
                q0.append((nx, ny))
            elif MAP[nx][ny] == '1' or MAP[nx][ny] == '#':
                visited[nx][ny] = True
                q1.append((nx, ny))
        
        if not q0:
            q0 = deque([e for e in q1])
            cnt += 1
            q1 = deque()
    print(cnt)