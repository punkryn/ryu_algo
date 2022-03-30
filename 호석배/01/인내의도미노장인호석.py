# https://www.acmicpc.net/problem/20165
import sys
si = sys.stdin.readline

dxy = {
    'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)
}

def DFS(x, y, d):
    ret = 0
    h = grid[x][y]
    if grid[x][y] > 0:
        ret += 1
        grid[x][y] *= -1
    for i in range(1, h):
        nx = x + dxy[d][0] * i
        ny = y + dxy[d][1] * i
        if not (0 <= nx < n and 0 <= ny < m): continue
        if grid[nx][ny] < 0: continue
        ret += DFS(nx, ny, d)
    
    return ret

if __name__ == '__main__':
    n, m, r = map(int, si().split())
    grid = [list(map(int, si().split())) for _ in range(n)]
    actions = [si().split() for _ in range(r * 2)]
    ans = 0
    for i in range(r * 2):
        if i % 2 == 0:
            x, y, d = actions[i]
            x, y = int(x), int(y)
            ans += DFS(x - 1, y - 1, d)
        else:
            x, y = map(int, actions[i])
            grid[x - 1][y - 1] = abs(grid[x - 1][y - 1])
    
    print(ans)
    for i in range(n):
        for j in range(m):
            if grid[i][j] < 0:
                print('F', end=' ')
            else:
                print('S', end=' ')
        print()