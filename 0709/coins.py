# https://www.acmicpc.net/problem/3067
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    coins = list(map(int, si().split()))
    m = int(si())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], m + 1):
            dp[j] += dp[j - coins[i]]
    print(dp[m])

if __name__ == '__main__':
    for _ in range(int(si())):
        main()