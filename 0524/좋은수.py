# https://www.acmicpc.net/problem/5624
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    dp = [0] * 400010
    ans = 0
    for i in range(n):
        for j in range(i):
            if dp[a[i] - a[j] + 200000]:
                ans += 1
                break
        
        for j in range(i + 1):
            dp[a[i] + a[j] + 200000] = 1
    print(ans)