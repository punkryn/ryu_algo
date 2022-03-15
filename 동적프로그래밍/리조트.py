import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    days = list(map(int, si().split()))
    holiday = [0] * (n + 1)
    for day in days:
        holiday[day] = 1

    dp = [[int(1e9)] * 50 for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in [1, 3, 5]:
            for k in range(41):
                if j == 1:
                    if holiday[i]:
                        dp[i][k] = dp[i-1][k]
                        continue
                    dp[i][k] = min(dp[i][k], dp[i-1][k] + 10000, dp[i-1][k+3])
                elif j == 3:
                    if i - 3 < 0 or k - 1 < 0:
                        continue
                    dp[i][k] = min(dp[i][k], dp[i-3][k - 1] + 25000)
                elif j == 5:
                    if i - 5 < 0 or k - 2 < 0:
                        continue
                    dp[i][k] = min(dp[i][k], dp[i - 5][k - 2] + 37000)
    ans = min(dp[n])
    print(ans)

if __name__ == '__main__':
    main()