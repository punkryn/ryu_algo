import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y, depth, total):
    global ans
    if depth == height:
        ans = max(ans, total)
        return
    
    if y >= n:
        x += 1
        y = 0
    
    if x >= n: 
        return

    if visited[x][y]:
        go(x, y + 1, depth, total)
        return


    go(x, y + 1, depth, total)
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] != 0: continue
        visited[nx][ny] = 1
        go(x, y + 1, depth + 1, total + grid[nx][ny] + grid[x][y])
        visited[nx][ny] = 0
    visited[x][y] = 0

if __name__ == '__main__':
    n = int(si())
    grid = [list(map(int, si().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0
    height = 2 if n <= 2 else 4
    go(0, 0, 0, 0)
    print(ans)