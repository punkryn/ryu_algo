# https://www.acmicpc.net/problem/1445
import sys
import heapq
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = map(int, si().split())
    MAP = list(si().strip() for _ in range(n))
    
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 'S':
                start = (i, j)
            elif MAP[i][j] == 'F':
                end = (i, j)
            
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = 0
    q = []
    q.append((0, 0, start[0], start[1]))
    while q:
        g_cnt, g_around, x, y = heapq.heappop(q)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == end[0] and ny == end[1]:
                print(g_cnt, g_around)
                exit()

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            if MAP[nx][ny] == 'g':
                heapq.heappush(q, (g_cnt + 1, g_around, nx, ny))
            elif MAP[nx][ny] == '.':
                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]
                    if not (0 <= nnx < n and 0 <= nny < m): continue
                    if MAP[nnx][nny] == 'g':
                        heapq.heappush(q, (g_cnt, g_around + 1, nx, ny))
                        break
                else:
                    heapq.heappush(q, (g_cnt, g_around, nx, ny))