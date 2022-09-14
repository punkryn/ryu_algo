# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, k):
    visited[x][y] = k
    
    q = deque([(x, y)])

    cand = [(x, y)]
    cnt = 1
    SUM = a[x][y]
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny] != 0: continue

            d = abs(a[x][y] - a[nx][ny])
            if not (l <= d <= r): continue
            
            visited[nx][ny] = k
            q.append((nx, ny))
            cand.append((nx, ny))
            cnt += 1
            SUM += a[nx][ny]
    
    calc = SUM // cnt
    for x, y in cand:
        a[x][y] = calc
    
    return cnt != 1


if __name__ == '__main__':
    n, l, r = mis()
    a = [list(mis()) for _ in range(n)]

    ans = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        
        k = 1
        flag = False
        for i in range(n):
            for j in range(n):
                if visited[i][j] != 0: continue
                flag |= bfs(i, j, k)
                k += 1
        
        if flag:
            ans += 1
        else:
            break
    print(ans)