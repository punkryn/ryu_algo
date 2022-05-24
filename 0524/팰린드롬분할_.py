# https://www.acmicpc.net/problem/1509
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    s = si().rstrip()
    n = len(s)
    p = [[False] * (n) for _ in range(n)]
    for i in range(n):
        p[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            p[i][i + 1] = True
    
    for i in range(3, n + 1):
        for j in range(n - 2):
            length = j + i - 1
            if length >= n: continue
            if s[j] == s[length] and p[j + 1][length - 1]:
                p[j][length] = True
    
    dp = [0] * n
    for end in range(n):
        dp[end] = int(1e6)
        for start in range(end + 1):
            if p[start][end]:
                if start == 0:
                    dp[end] = 1
                else:
                    dp[end] = min(dp[end], dp[start - 1] + 1)
    print(dp[n - 1])