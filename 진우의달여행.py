# https://www.acmicpc.net/problem/17485
import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    matrix = [0] + [[0] + list(map(int, si().split())) + [0] for _ in range(n)] + [0]
    dp = [[[0, 0, 0] for _ in range(m + 2)] for _ in range(n + 2)]

    for i in range(m):
        for j in range(3):
            dp[1][i][j] = matrix[1][i]
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + matrix[i][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + matrix[i][j]
    print(dp[-1])

if __name__ == '__main__':
    main()