# https://acmicpc.net/problem/9465
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    a = [list(map(int, si().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]
    
    if n>=2:
        dp[0][1] = a[1][0] + a[0][1]
        dp[1][1] = a[0][0] + a[1][1]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + a[0][i], dp[0][i-2] + a[0][i], dp[1][i-2] + a[0][i])
        dp[1][i] = max(dp[0][i-1] + a[1][i], dp[0][i-2] + a[1][i], dp[1][i-2] + a[1][i])
    print(max(dp[0][n-1], dp[1][n-1]))

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()