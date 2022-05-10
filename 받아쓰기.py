# https://www.acmicpc.net/problem/20542
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    s = si().strip()
    a = si().strip()
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        dp[i][0] = i
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

            if s[i - 1] == a[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

            if (s[i - 1] in ['i'] and a[j - 1] in ['i', 'j', 'l']):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        
            if s[i - 1] in ['v'] and a[j - 1] in ['v', 'w']:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
    
    print(dp[n][m])