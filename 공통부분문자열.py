# https://www.acmicpc.net/problem/5582
import sys
si = sys.stdin.readline

def main():
    s1 = si().strip()
    s2 = si().strip()

    dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    ans = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])
    print(ans)

if __name__ == '__main__':
    main()