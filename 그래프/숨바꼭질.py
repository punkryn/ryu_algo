# https://www.acmicpc.net/problem/1697
import sys
si = sys.stdin.readline

def main():
    global ans
    n, k = map(int, si().split())
    dp = [0] * 100010
    for i in range(n-1, -1, -1):
        dp[i] = n - i
    if n < k:
        for i in range(n + 1, min(k + k, 100002)):
            if i % 2 == 0:
                dp[i] = min(dp[i // 2] + 1, dp[i-1] + 1)
            else:
                dp[i] = dp[i-1] + 1
        
        for i in range(n + 1, k + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i // 2] + 1, dp[i-1] + 1, dp[i+1] + 1)
            else:
                dp[i] = min(dp[i-1] + 1, dp[i+1] + 1)

        # print(dp[:k+1])
        print(dp[k])
    else:
        print(n - k)
    # print(dp[:k + 1])

if __name__ == '__main__':
    main()