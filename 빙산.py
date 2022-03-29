# https://www.acmicpc.net/problem/2573
import sys
import heapq
from collections import deque
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs(start, number):
    q.append(start)

    while q:
        cur = q.popleft()
        visited[cur[0]][cur[1]] = number

        for i in range(4):
            x, y = cur
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            if MAP[nx][ny] == 0:
                count[x][y] += 1
                continue

            if visited[nx][ny] != 0:
                continue

            visited[nx][ny] = number
            q.append((nx, ny))

if __name__ == '__main__':
    n, m = map(int, si().split())
    MAP = [list(map(int, si().split())) for _ in range(n)]
    
    ans = 0
    while True:
        visited = [[0] * m for _ in range(n)]
        count = [[0] * m for _ in range(n)]
        num = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if MAP[i][j] > 0 and visited[i][j] == 0:
                    num += 1
                    bfs((i, j), num)

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                MAP[i][j] = max(0, MAP[i][j] - count[i][j])

        if num > 1:
            break
        elif num == 0:
            ans = 0
        ans += 1
    
    print(ans)