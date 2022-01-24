# https://acmicpc.net/problem/1562
import sys

def main():
    n = int(sys.stdin.readline())
    dp = [[[[0 for _4 in range(10)] for _3 in range(10)] for _2 in range(10)] for _1 in range(n + 1)]
    MOD = 1000000000

    for num in range(1, 10):
        dp[1][num][num][num] = 1

    for len in range(2, n + 1):
        for prev in range(10):
            for low in range(10):
                for high in range(10):
                    for cur in [prev - 1, prev + 1]:
                        if cur < 0 or cur > 9: continue
                        dp[len][cur][min(low, cur)][max(high, cur)] += dp[len - 1][prev][low][high]
                        dp[len][cur][min(low, cur)][max(high, cur)] %= MOD

    ans = 0
    for i in range(10):
        ans += dp[n][i][0][9]
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()