# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, n, num, MAP):
    visited[x][y] = num
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and MAP[nx][ny] == '1':
                cnt += dfs(nx, ny, visited, n, num, MAP)
    return cnt

def bfs(x, y, visited, n, num, MAP):
    q = deque()
    q.append((x, y))
    visited[x][y] = num
    cnt = 1
    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and MAP[nx][ny] == '1':
                    visited[nx][ny] = num
                    cnt += 1
                    q.append((nx, ny))
    return cnt

def main():
    n = int(si())
    MAP = [si().strip() for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    
    num = 0
    ans = []
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == '1' and visited[i][j] == 0:
                num += 1
                # ans.append(bfs(i, j, visited, n, num, MAP))
                ans.append(dfs(i, j, visited, n, num, MAP))

    # for v in visited:
    #     print(v)
    print(num)    
    for a in sorted(ans):
        print(a)

if __name__ == '__main__':
    main()