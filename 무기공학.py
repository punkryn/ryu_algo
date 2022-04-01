# https://www.acmicpc.net/problem/18430
from os import defpath
import sys
sys.setrecursionlimit(1000000)
si = sys.stdin.readline

# def go(r, c, v):
#     global ans
#     for x in range(n):
#         for y in range(m):
#             if r < x and c < y: continue
#             if visited[x][y] != 0: continue

#             visited[x][y] = 1
            # for nx1, ny1, nx2, ny2 in [(x + 1, y, x, y - 1), (x - 1, y, x, y - 1), (x - 1, y, x, y + 1), (x + 1, y, x, y + 1)]:
            #     if not (0 <= nx1 < n and 0 <= ny1 < m): continue
            #     if not (0 <= nx2 < n and 0 <= ny2 < m): continue
            #     if visited[nx1][ny1] or visited[nx2][ny2] != 0: continue
            #     total = material[x][y] * 2 + material[nx1][ny1] + material[nx2][ny2]
            #     visited[nx1][ny1] = 1
            #     visited[nx2][ny2] = 1
            #     go(r, c, v + total)
            #     visited[nx2][ny2] = 0
            #     visited[nx1][ny1] = 0
#             visited[x][y] = 0
    
#     ans = max(ans, v)
#     return

# def go(depth, v):
#     global ans
#     if depth == n * m:
#         ans = max(ans, v)
#         return

#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j] != 0: continue
#             # if i < r - 1 and j < c - 1: continue
#             cnt += 1
#             visited[i][j] = 1
#             for x1, y1, x2, y2 in [(i-1, j, i, j - 1), (i, j - 1, i + 1, j), (i + 1, j, i, j + 1), (i - 1, j, i, j + 1)]:
#                 if not (0 <= x1 < n and 0 <= y1 < m) or not (0 <= x2 < n and 0 <= y2 < m): continue
#                 if visited[x1][y1] != 0 or visited[x2][y2] != 0: continue
#                 visited[x1][y1] = 1
#                 visited[x2][y2] = 1
#                 total = material[i][j] * 2 + material[x1][y1] + material[x2][y2]
#                 go(cnt, v + total)
#                 visited[x2][y2] = 0
#                 visited[x1][y1] = 1
#             visited[i][j] = 0
#             go(cnt, v)
#     abc=1

def go(depth, v, prev):
    global ans
    if depth == 0:
        ans = max(ans, v)
        return
    
    for i in range(prev + 1, nm - depth + 1):
        x = i // m
        y = i - (x * m)
        print(i, x, y)
        if visited[x][y] != 0:
            continue
        
        visited[x][y] = 1
        for nx1, ny1, nx2, ny2 in [(x + 1, y, x, y - 1), (x - 1, y, x, y - 1), (x - 1, y, x, y + 1), (x + 1, y, x, y + 1)]:
            if not (0 <= nx1 < n and 0 <= ny1 < m): continue
            if not (0 <= nx2 < n and 0 <= ny2 < m): continue
            if visited[nx1][ny1] != 0 or visited[nx2][ny2] != 0: continue
            total = material[x][y] * 2 + material[nx1][ny1] + material[nx2][ny2]
            visited[nx1][ny1] = 1
            visited[nx2][ny2] = 1
            go(depth - 1, v + total, i)
            visited[nx2][ny2] = 0
            visited[nx1][ny1] = 0
        visited[x][y] = 0
        go(depth - 1, v, i)
        abc = 1

if __name__ == '__main__':
    n, m = map(int, si().split())
    material = [list(map(int, si().split())) for _ in range(n)]
    nm = n * m
    visited = [[0] * m for _ in range(n)]
    ans = 0
    go(nm, 0, -1)
    print(ans)