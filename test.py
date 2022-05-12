from sys import stdin
si = stdin.readline

def move(s, e):
    if s == e: return 1
    elif s == 0: return 2
    elif abs(s - e) % 2 == 0: return 4
    else: return 3

if __name__ == '__main__':
    INF = int(1e9)
    a = list(map(int, si().split()))
    n = len(a)
    dp = [[INF] * 5 for _ in range(n)]
    for i in range(5):
        dp[0][i] = 0
    dp[1][0] = 0
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = dp[i - 1][j] + move(a[i - 2], a[i - 1])
        
        for j in range(5):
            dp[i][a[i - 2]] = min(dp[i][a[i - 2]], dp[i - 1][j] + move(j, a[i - 1]))
    print(dp)
    print(min(dp[n - 1]))