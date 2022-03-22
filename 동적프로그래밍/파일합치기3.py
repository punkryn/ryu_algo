# https://www.acmicpc.net/problem/11066
import sys
si = sys.stdin.readline
INF = int(1e9)
def main():
    k = int(si())
    sizes = list(map(int, si().split()))

    SUM = [0] * (k + 1)
    for i in range(1, k + 1):
        SUM[i] = SUM[i - 1] + sizes[i - 1]
    
    dp = [[INF] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        dp[i][i] = 0
        
    for d in range(1, k):
        for x in range(1, k - d + 1):
            for y in range(x, x + d):
                dp[x][x + d] = min(dp[x][x + d], dp[x][y] + dp[y + 1][x + d] + SUM[x + d] - SUM[x - 1])
            
    print(dp[1][k])

if __name__ == '__main__':
    for _ in range(int(si())):
        main()