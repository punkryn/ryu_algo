# https://www.acmicpc.net/problem/2937
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    grid = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, si().split())
        grid[a - 1][b - 1] = 1
    
    ps = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tmp1 = ps[i - 1][j]
            tmp2 = ps[i][j - 1]
            tmp3 = ps[i - 1][j - 1]
            ps[i][j] = tmp1 + tmp2 - tmp3 + grid[i - 1][j - 1]
    
    ans = int(1e9)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            k = 1
            while k * k <= m:
                if m % k != 0 or i + k - 1 > n or j + m // k - 1 > n:
                    k += 1
                    continue
                
                x1, x2 = i, i + k - 1
                y1, y2 = j, j + m // k - 1
                ans = min(ans, m - (ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]))
                k += 1
            
    print(ans)
