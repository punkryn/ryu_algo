import sys
MOD = 9901
def main():
    n = int(sys.stdin.readline())
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1
    
    for i in range(2, n + 1):
        dp[i][0] = sum(dp[i-1]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
    
    print(sum(dp[n]) % MOD)

if __name__ == '__main__':
    main()