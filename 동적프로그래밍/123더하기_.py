# acmicpc.net/problem/9095
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    # dp = [[0, 0, 0] for _ in  range(n + 1)]
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()