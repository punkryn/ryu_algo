# https://www.acmicpc.net/problem/13250
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())

    dp = [0] * (n + 10)
    for i in range(n - 1, -1, -1):
        ret = 0
        for j in range(1, 7):
            ret += (dp[i + j] + 1) / 6
        dp[i] = ret

    print(f'{dp[0]:.9f}')