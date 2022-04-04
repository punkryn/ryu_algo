# https://www.acmicpc.net/problem/18430
import sys
sys.setrecursionlimit(1000000)
si = sys.stdin.readline

# def go(depth, v, prev):
#     global ans

#     if depth == 0:
#         ans = max(ans, v)
#         return

#     for i in range(prev + 1, nm):
#         x = i // m
#         y = i - (x * m)
#         if visited[x][y] != 0:
#             continue
        
#         visited[x][y] = 1
#         for nx1, ny1, nx2, ny2 in [(x + 1, y, x, y - 1), (x - 1, y, x, y - 1), (x - 1, y, x, y + 1), (x + 1, y, x, y + 1)]:
#             if not (0 <= nx1 < n and 0 <= ny1 < m): continue
#             if not (0 <= nx2 < n and 0 <= ny2 < m): continue
#             if visited[nx1][ny1] != 0 or visited[nx2][ny2] != 0: continue
#             total = material[x][y] * 2 + material[nx1][ny1] + material[nx2][ny2]
#             visited[nx1][ny1] = 1
#             visited[nx2][ny2] = 1
#             go(depth - 1, v + total, i)
#             visited[nx2][ny2] = 0
#             visited[nx1][ny1] = 0
#         visited[x][y] = 0
#         go(depth - 1, v, i)

def go(x, y, v):
    global ans
    if y == m:
        y = 0
        x += 1
    
    if x == n:
        ans = max(ans, v)
        return
    
    if not visited[x][y]:
        if x + 1 < n and y - 1 >= 0 and not visited[x + 1][y] and not visited[x][y - 1]:
            visited[x][y] = 1
            visited[x + 1][y] = 1
            visited[x][y - 1] = 1
            total = material[x][y] * 2 + material[x + 1][y] + material[x][y - 1]
            go(x, y + 1, v + total)
            visited[x][y - 1] = 0
            visited[x + 1][y] = 0
            visited[x][y] = 0
        if x - 1 >= 0 and y - 1 >= 0 and not visited[x - 1][y] and not visited[x][y - 1]:
            visited[x][y] = 1
            visited[x - 1][y] = 1
            visited[x][y - 1] = 1
            total = material[x][y] * 2 + material[x - 1][y] + material[x][y - 1]
            go(x, y + 1, v + total)
            visited[x][y - 1] = 0
            visited[x - 1][y] = 0
            visited[x][y] = 0
        if x - 1 >= 0 and y + 1 < m and not visited[x - 1][y] and not visited[x][y + 1]:
            visited[x][y] = 1
            visited[x - 1][y] = 1
            visited[x][y + 1] = 1
            total = material[x][y] * 2 + material[x - 1][y] + material[x][y + 1]
            go(x, y + 1, v + total)
            visited[x][y + 1] = 0
            visited[x - 1][y] = 0
            visited[x][y] = 0
        if x + 1 < n and y + 1 < m and not visited[x + 1][y] and not visited[x][y + 1]:
            visited[x][y] = 1
            visited[x + 1][y] = 1
            visited[x][y + 1] = 1
            total = material[x][y] * 2 + material[x + 1][y] + material[x][y + 1]
            go(x, y + 1, v + total)
            visited[x][y + 1] = 0
            visited[x + 1][y] = 0
            visited[x][y] = 0
        
    go(x, y + 1, v)
    return
        
        

if __name__ == '__main__':
    n, m = map(int, si().split())
    material = [list(map(int, si().split())) for _ in range(n)]
    nm = n * m
    visited = [[0] * m for _ in range(n)]
    ans = 0
    go(0, 0, 0)
    print(ans)