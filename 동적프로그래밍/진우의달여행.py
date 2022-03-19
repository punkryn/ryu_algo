# https://www.acmicpc.net/problem/17485
import sys
si = sys.stdin.readline
INF = int(1e9)
def main():
    n, m = map(int, si().split())
    matrix = [list(map(int, si().split())) + [0] for _ in range(n)]
    dp = [[[INF, INF, INF] for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(3):
            dp[0][i][j] = matrix[0][i]
    
    for i in range(1, n):
        for j in range(m):
            if j - 1 >= 0:
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + matrix[i][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i][j]
            if j + 1 < m:
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + matrix[i][j]

    ans = INF        
    for x in dp[-1]:
        ans = min(ans, min(x))
    print(ans)

if __name__ == '__main__':
    main()