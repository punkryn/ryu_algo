# https://acmicpc.net/problem/2156
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    amount = [0] + [int(si()) for _ in range(n)]
    dp = [[0, 0] for _ in range(n + 1)]
    
    dp[1][0] = amount[1]
    if n >= 2:
        dp[2][0], dp[2][1] = amount[1] + amount[2], amount[2]
    
    for i in range(3, n + 1):
        dp[i][0] = dp[i-1][1] + amount[i]
        dp[i][1] = max(dp[i-2][0] + amount[i], dp[i-2][1] + amount[i])
        dp[i][1] = max(dp[i][1], max(dp[i-3][0] + amount[i], dp[i-3][1] + amount[i]))
    
    ans = max(dp[n])
    if ans >= 2:
        ans = max(ans, max(dp[n-1]))
        
    print(ans)

if __name__ == '__main__':
    main()