dp = [0] * 20
dp[0] = 1
for i in range(1, 16):
    dp[i] = dp[i - 1] * i
print(dp)

ans = 0
for i in range(1, 16):
    ans += dp[15] // (dp[15 - i] * dp[i])
print(ans)