# https://acmicp.net/problem/1309
import sys

def main():
    n = int(sys.stdin.readline())
    dp = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]
    # print(len(dp), len(dp[0][0]))
    if n == 1:
        print(3)
    else:
        dp[1][0][0], dp[1][0][1], dp[1][1][0], dp[1][1][1] = 1, 2, 1, 2
        dp[2][0][0], dp[2][0][1], dp[2][1][0], dp[2][1][1] = 2, 3, 2, 3
        for i in range(3, n + 1):
            tmp1 = (dp[i-1][0][0] + dp[i-1][0][1]) % 9901
            dp[i][0][0], dp[i][1][0] = tmp1, tmp1
            tmp = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][1][0]) % 9901
            dp[i][0][1], dp[i][1][1] = tmp, tmp
        
        print((dp[n][0][0] + dp[n][0][1] + dp[n][1][0]) % 9901)

if __name__ == '__main__':
    main()