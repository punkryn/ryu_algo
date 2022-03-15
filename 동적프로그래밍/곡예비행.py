# https://acmicpc.net/problem/21923

import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    up = [[0] * m for _ in range(n)]
    up[n-1][0] = matrix[n-1][0]
    down = [[0] * m for _ in range(n)]
    down[n-1][m-1] = matrix[n-1][m-1]

    for i in range(n-1, -1, -1):
        for j in range(m):
            if i == n-1 and j == 0:
                continue

            if i == n-1:
                up[i][j] = matrix[i][j] + up[i][j-1]
            elif j == 0:
                up[i][j] = matrix[i][j] + up[i+1][j]
            else:
                up[i][j] = matrix[i][j] + max(up[i+1][j], up[i][j-1])
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                continue

            if i == n-1:
                down[i][j] = matrix[i][j] + down[i][j+1]
            elif j == m-1:
                down[i][j] = matrix[i][j] + down[i+1][j]
            else:
                down[i][j] = matrix[i][j] + max(down[i+1][j], down[i][j+1])
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                ans = up[i][j] + down[i][j]
                continue

            ans = max(ans, up[i][j] + down[i][j])
    print(ans)

if __name__ == '__main__':
    main()