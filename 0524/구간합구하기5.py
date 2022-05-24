# https://www.acmicpc.net/problem/11660
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [list(map(int, si().split())) for _ in range(n)]
    ps = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ps[i][j] = ps[i][j - 1] + grid[i - 1][j - 1]
    
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            ps[i][j] += ps[i - 1][j]
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, si().split())
        print(ps[x2][y2] - ps[x2][y1 - 1] - ps[x1 - 1][y2] + ps[x1 - 1][y1 - 1])