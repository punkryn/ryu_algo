# https://www.acmicpc.net/problem/17141
import sys
from itertools import combinations
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(vir):
    q = deque(vir)
    visited = [[-1] * n for _ in range(n)]
    for x,y in vir:
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] != -1:
                continue
            if lab[nx][ny] == 1:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    
    mv = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 1: continue
            if visited[i][j] == -1:
                return -1
            
            mv = max(mv, visited[i][j])
    return mv
        

if __name__ == '__main__':
    n, m = map(int, si().split())
    lab = [list(map(int, si().split())) for _ in range(n)]
    pos = [(i, j) for i in range(n) for j in range(n) if lab[i][j] == 2]
    ans = int(1e9)
    for comb in combinations(pos, m):
        ret = bfs(comb)
        if ret == -1:
            continue
        
        ans = min(ans, ret)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)