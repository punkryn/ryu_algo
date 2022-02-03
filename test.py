dp = [[0] * (26) for _ in range(26)]
dp[1][1] = 1
for i in range(1, 26):
    for j in range(1, 26):
        if i == 1 and j == 1: continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])