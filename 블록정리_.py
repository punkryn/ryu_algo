# https://www.acmicpc.net/problem/2937
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        r, c = map(int, si().split())
        grid[r][c] = 1
    
    ps = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + grid[i][j]
    
    ans = int(1e9)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            k = 1
            while k * k <= m:
                if m % k != 0 or i + k - 1 > n or j + m // k - 1 > n:
                    k += 1
                    continue

                x1, y1 = i, j
                x2, y2 = i + k - 1, j + m // k - 1
                
                ans = min(ans, m - (ps[x2][y2] - ps[x2][y1 - 1] - ps[x1 - 1][y2] + ps[x1 - 1][y1 - 1]))
                k += 1
    print(ans)