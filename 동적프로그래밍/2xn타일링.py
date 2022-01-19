# https://acmicpc.net/problem/11726
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    dp = [0, 1, 2] + [0] * (n - 2)
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[n])

if __name__ == '__main__':
    main()