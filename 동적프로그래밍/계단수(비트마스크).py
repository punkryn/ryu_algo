import sys

def main():
    n = int(sys.stdin.readline())
    MOD = 1000000000
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    FULL = (1 << 10) - 1
    for length in range(2, n + 1):
        for i in range(10):
            for j in range(FULL + 1):
                if i == 0:
                    dp[length][i][j | 1 << i] = (dp[length][i][j | 1 << i] + dp[length-1][1][j]) % MOD
                elif i == 9:
                    dp[length][i][j | 1 << i] = (dp[length][i][j | 1 << i] + dp[length-1][8][j]) % MOD
                else:
                    dp[length][i][j | 1 << i] = (dp[length][i][j | 1 << i] + dp[length-1][i-1][j]) % MOD
                    dp[length][i][j | 1 << i] = (dp[length][i][j | 1 << i] + dp[length-1][i+1][j]) % MOD

    ans = 0
    for i in range(10):
        ans = (ans + dp[n][i][FULL]) % MOD

    print(ans)

if __name__ == '__main__':
    main()