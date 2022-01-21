# https://acmipc.net/problem/2688
import sys

def main():
    n = int(sys.stdin.readline())
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, 11):
        dp[1][i-1] = i
    
    for i in range(2, n + 1):
        dp[i][0] = 1
        for j in range(1, 10):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[n][9])

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        main()