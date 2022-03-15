# 시간 초과남

import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline

def main():
    INF = int(1e9)
    UP = 0
    DOWN = 1
    n, m = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    dy = [[[-INF] * 2 for _ in range(m)] for _ in range(n)]
    dy[n-1][0][UP] = matrix[n-1][0]

    def solve(i, j, st):
        if i < 0 or i > n-1 or j < 0 or j > m-1:
            return -INF
        
        if dy[i][j][st] != -INF:
            return dy[i][j][st]
        res = dy[i][j][st]

        if st == UP:
            res = max(solve(i+1, j, st), solve(i, j-1, st)) + matrix[i][j]
        else:
            res = max(solve(i-1, j, st), solve(i, j-1, st)) + matrix[i][j]
            res = max(res, solve(i, j, UP) + matrix[i][j])

        return res
    
    print(solve(n-1, m-1, DOWN))

if __name__ == '__main__':
    main()