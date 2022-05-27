# https://www.acmicpc.net/problem/9252
from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e9))
si = stdin.readline

def rev(x, y):
    global ans
    if dp[x][y] == 0:
        return

    if a[x - 1] == b[y - 1]:
        rev(x - 1, y - 1)
        ans += a[x - 1]
    elif dp[x - 1][y] > dp[x][y - 1]:
        rev(x - 1, y)
    else:
        rev(x, y - 1)

if __name__ == '__main__':
    b = si().strip()
    a = si().strip()
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (1 if a[i - 1] == b[j - 1] else 0))
    
    ans = ''
    x, y = len(a), len(b)
    while dp[x][y]:
        if a[x - 1] == b[y - 1]:
            ans += a[x - 1]
            x -= 1
            y -= 1
        elif dp[x - 1][y] > dp[x][y - 1]:
            x -= 1
        else:
            y -= 1
    # rev(len(a), len(b))
    
    print(dp[-1][-1])
    print(ans[::-1])